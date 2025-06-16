from pydantic import BaseModel, Field
from datetime import date, time
from typing import Optional, List

# Base para crear y reutilizar
class ProduccionEmbrionariaBase(BaseModel):
    cliente_id: int
    fecha_opu: date
    lugar: str
    hora_inicio: Optional[time] = None
    hora_final: Optional[time] = None
    envase: str
    fecha_transferencia: date  # Calculado como fecha_opu + 7 días

# Crear una nueva producción embrionaria
class ProduccionEmbrionariaCreate(ProduccionEmbrionariaBase):
    pass

# Actualizar producción embrionaria
class ProduccionEmbrionariaUpdate(BaseModel):
    fecha_opu: Optional[date] = None
    lugar: Optional[str] = None
    hora_inicio: Optional[time] = None
    hora_final: Optional[time] = None
    envase: Optional[str] = None
    fecha_transferencia: Optional[date] = None

# Datos internos del modelo (incluye ID y timestamps)
class ProduccionEmbrionariaInDB(ProduccionEmbrionariaBase):
    id: int
    created_at: date
    updated_at: date

    class Config:
        orm_mode=True
        from_attributes = True
        

# Vista detallada de la producción embrionaria (con nombres de entidades relacionadas)
class ProduccionEmbrionariaDetail(ProduccionEmbrionariaInDB):
    cliente_nombre: Optional[str]
    total_opus: Optional[int]

    class Config:
        orm_mode = True

# Resumen por fecha
class ProduccionEmbrionariaResumenPorFecha(BaseModel):
    fecha_opu: date
    cliente_nombre: str
    total_producciones: int
    total_opus: int

    class Config:
        from_attributes = True

# Detalle de la producción embrionaria con lista de opus asociados (opcional si lo necesitas)
from .opus_schema import OpusInDB

class ProduccionEmbrionariaWithOpus(ProduccionEmbrionariaDetail):
    opus: List[OpusInDB]
