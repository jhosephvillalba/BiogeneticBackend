from fastapi import APIRouter, Depends, HTTPException, status, Request, Query
from sqlalchemy.orm import Session
from typing import List
from datetime import date
import logging

from app.database.base import get_db
from app.services import produccion_embrionaria_service
from app.services.auth_service import get_current_user_from_token
from app.schemas.produccion_embrionaria import (
    ProduccionEmbrionariaCreate,
    ProduccionEmbrionariaInDB,
    ProduccionEmbrionariaDetail
)

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

@router.get("/{produccion_id}/opus", response_model=List[dict])
async def get_opus_by_produccion(
    produccion_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token)
):
    """
    Obtener todos los registros Opus asociados a una producción embrionaria específica.
    """
    try:
        return produccion_embrionaria_service.get_by_cliente(db, produccion_id, current_user)
    except Exception as e:
        logging.error(f"Error al obtener opus de la producción {produccion_id}: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener opus: {str(e)}"
        )
