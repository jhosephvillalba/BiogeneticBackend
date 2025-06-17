from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import timedelta
from app.services import role_service
from datetime import datetime

from app.models.opus import ProduccionEmbrionaria
from app.schemas.produccion_embrionaria import (
    ProduccionEmbrionariaCreate,
    ProduccionEmbrionariaUpdate,
)

from app.models.user import User
from sqlalchemy import or_



def get_all(
    db: Session,
    current_user: User,
    fecha_inicio: datetime = None,
    fecha_fin: datetime = None,
    query: str = None
):
    # 🔐 Verificar si es administrador
    if not role_service.is_admin(current_user):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No autorizado")

    q = db.query(ProduccionEmbrionaria).join(ProduccionEmbrionaria.cliente)

    # 🗓️ Filtros por fecha
    if fecha_inicio:
        q = q.filter(ProduccionEmbrionaria.fecha >= fecha_inicio)
    if fecha_fin:
        q = q.filter(ProduccionEmbrionaria.fecha <= fecha_fin)

    # 🔍 Filtro por nombre o documento
    if query:
        q = q.filter(
            or_(
                ProduccionEmbrionaria.cliente.has(User.full_name.ilike(f"%{query}%")),
                ProduccionEmbrionaria.cliente.has(User.number_document.ilike(f"%{query}%")),
                ProduccionEmbrionaria.cliente.has(User.email.ilike(f"%{query}%"))
            )
        )

    return q.all()



def get_by_id(db: Session, produccion_id: int):
    produccion = db.query(ProduccionEmbrionaria).filter(ProduccionEmbrionaria.id == produccion_id).first()
    if not produccion:
        raise HTTPException(status_code=404, detail="Producción no encontrada")
    return produccion


def get_by_cliente(db: Session, cliente_id: int):
    return db.query(ProduccionEmbrionaria).filter(ProduccionEmbrionaria.cliente_id == cliente_id).all()


def create(db: Session, data: ProduccionEmbrionariaCreate):
    # Calcular fecha_transferencia
    fecha_transferencia = data.fecha_opu + timedelta(days=7)

    nueva_produccion = ProduccionEmbrionaria(
        cliente_id=data.cliente_id,
        fecha_opu=data.fecha_opu,
        output_id=data.output_id,
        lugar=data.lugar,
        finca=data.finca,
        hora_inicio=data.hora_inicio,
        hora_final=data.hora_final,
        envase=data.envase,
        fecha_transferencia=fecha_transferencia
    )

    db.add(nueva_produccion)
    db.commit()
    db.refresh(nueva_produccion)
    return nueva_produccion


def update(db: Session, produccion_id: int, data: ProduccionEmbrionariaUpdate):

    produccion = get_by_id(db, produccion_id)

    for field, value in data.dict(exclude_unset=True).items():
        setattr(produccion, field, value)

    # Si se actualiza fecha_opu, recalcular fecha_transferencia si no fue pasada explícitamente
    if "fecha_opu" in data.dict(exclude_unset=True) and "fecha_transferencia" not in data.dict(exclude_unset=True):
        produccion.fecha_transferencia = produccion.fecha_opu + timedelta(days=7)

    db.commit()
    db.refresh(produccion)
    return produccion


def delete(db: Session, produccion_id: int):
    produccion = get_by_id(db, produccion_id)
    db.delete(produccion)
    db.commit()
    return {"ok": True}
