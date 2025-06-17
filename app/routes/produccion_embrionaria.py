from fastapi import APIRouter, Depends, HTTPException, status, Request, Query
from sqlalchemy.orm import Session
from typing import List
from datetime import date, datetime
import logging

from app.database.base import get_db
from app.services import produccion_embrionaria_service
from app.services.auth_service import get_current_user_from_token
from app.schemas.produccion_embrionaria import (
    ProduccionEmbrionariaCreate,
    ProduccionEmbrionariaInDB,
    ProduccionEmbrionariaDetail,
    ProduccionEmbrionariaUpdate
)
from typing import Optional

from app.models.user import User

router = APIRouter(
    prefix="/produccion-embrionaria",
    tags=["produccion-embrionaria"],
    responses={404: {"description": "No encontrado"}},
)

@router.post("/", response_model=ProduccionEmbrionariaInDB, status_code=status.HTTP_201_CREATED)
async def create_produccion_embrionaria(
    data: ProduccionEmbrionariaCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token)
):
    """
    Crear una producción embrionaria para un cliente específico (solo admin).
    """
    try:
        if not produccion_embrionaria_service.role_service.is_admin(current_user):
            raise HTTPException(status_code=403, detail="No autorizado")

        return produccion_embrionaria_service.create(db, data)
    except Exception as e:
        logging.error(f"Error al crear producción embrionaria: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error al crear producción embrionaria: {str(e)}"
        )
    


@router.put("/{production_id}", response_model=ProduccionEmbrionariaUpdate, status_code=status.HTTP_200_OK)
async def create_produccion_embrionaria(
    production_id:int,
    data: ProduccionEmbrionariaUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token)
):
    """
    Crear una producción embrionaria para un cliente específico (solo admin).
    """
    try:
        if not produccion_embrionaria_service.role_service.is_admin(current_user):
            raise HTTPException(status_code=403, detail="No autorizado")

        return produccion_embrionaria_service.update(db, production_id, data)
    except Exception as e:
        logging.error(f"Error al crear producción embrionaria: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error al crear producción embrionaria: {str(e)}"
        )
    




@router.get("/mis", response_model=List[ProduccionEmbrionariaDetail])
async def get_my_producciones_embrionarias(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token)
):
    """
    Listar todas las producciones embrionarias del cliente autenticado.
    """
    try:
        return produccion_embrionaria_service.get_by_cliente(db, current_user.id)
    except Exception as e:
        logging.error(f"Error al obtener producciones embrionarias del cliente: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener producciones embrionarias: {str(e)}"
        )


@router.get("/", response_model=List[ProduccionEmbrionariaInDB])
def get_producciones_admin(
    fecha_inicio: Optional[datetime] = Query(None),
    fecha_fin: Optional[datetime] = Query(None),
    query: Optional[str] = Query(None, description="Buscar por nombre o documento del cliente"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    return produccion_embrionaria_service.get_all(
        db=db,
        current_user=current_user,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        query=query
    )


@router.get("/{production_id}", response_model=ProduccionEmbrionariaDetail, status_code=status.HTTP_200_OK)
async def create_produccion_embrionaria(
    production_id:int,
    db: Session = Depends(get_db)
):
    """
    Crear una producción embrionaria para un cliente específico (solo admin).
    """
    try:
        # if not produccion_embrionaria_service.role_service.is_admin(current_user):
        #     raise HTTPException(status_code=403, detail="No autorizado")

        return produccion_embrionaria_service.get_by_id(db, production_id)
    except Exception as e:
        logging.error(f"Error al crear producción embrionaria: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error al crear producción embrionaria: {str(e)}"
        )