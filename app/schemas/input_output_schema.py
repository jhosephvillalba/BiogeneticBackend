from typing import Optional, List, Dict, Any, TYPE_CHECKING
from pydantic import BaseModel, Field, validator
from app.schemas.base_schema import BaseSchema
from datetime import datetime
from enum import Enum
from app.models.input_output import InputStatus as ModelInputStatus

if TYPE_CHECKING:
    from app.models.input_output import Input

# Esta clase es para validación de Pydantic
class InputStatus(str, Enum):
    pending = "Pending"
    processing = "Processing"
    completed = "Completed"
    cancelled = "Cancelled"
    
    @classmethod
    def from_model(cls, status: ModelInputStatus) -> "InputStatus":
        """Convierte de estado del modelo a estado del esquema"""
        if status == ModelInputStatus.pending:
            return cls.pending
        elif status == ModelInputStatus.processing:
            return cls.processing
        elif status == ModelInputStatus.completed:
            return cls.completed
        elif status == ModelInputStatus.cancelled:
            return cls.cancelled
        return cls.pending
        
    def to_model(self) -> ModelInputStatus:
        """Convierte de estado del esquema a estado del modelo"""
        if self == InputStatus.pending:
            return ModelInputStatus.pending
        elif self == InputStatus.processing:
            return ModelInputStatus.processing
        elif self == InputStatus.completed:
            return ModelInputStatus.completed
        elif self == InputStatus.cancelled:
            return ModelInputStatus.cancelled
        return ModelInputStatus.pending

class InputBase(BaseModel):
    quantity_received: float = Field(..., gt=0, description="Cantidad recibida - debe ser mayor que 0")
    bull_id: int
    user_id: int = Field(..., description="ID del usuario al que se asignará el input")
    quantity_taken: float = Field(0, ge=0, description="Cantidad tomada - debe ser mayor o igual a 0")
    escalarilla: Optional[str] = None
    lote: Optional[str] = None
    fv: Optional[datetime] = None
    
    @validator('quantity_taken')
    def validate_quantity_taken(cls, v, values):
        """Validar que la cantidad tomada no exceda la cantidad recibida"""
        if 'quantity_received' in values and v > values['quantity_received']:
            raise ValueError(f"La cantidad tomada ({v}) no puede ser mayor que la cantidad recibida ({values['quantity_received']})")
        return v

class InputCreate(InputBase):
    pass

class InputUpdate(BaseModel):
    quantity_received: Optional[float] = Field(None, gt=0, description="Cantidad recibida - debe ser mayor que 0")
    escalarilla: Optional[str] = None
    bull_id: Optional[int] = None
    status_id: Optional[InputStatus] = None
    lote: Optional[str] = None
    fv: Optional[datetime] = None
    quantity_taken: Optional[float] = Field(None, ge=0, description="Cantidad tomada - debe ser mayor o igual a 0")
    
    @validator('quantity_taken')
    def validate_quantity_taken(cls, v, values):
        """Validar que la cantidad tomada no exceda la cantidad recibida"""
        if v is not None and 'quantity_received' in values and values['quantity_received'] is not None and v > values['quantity_received']:
            raise ValueError(f"La cantidad tomada ({v}) no puede ser mayor que la cantidad recibida ({values['quantity_received']})")
        return v

class InputFilter(BaseModel):
    """Modelo para filtrar inputs por diversos criterios"""
    document_number: Optional[str] = None
    user_name: Optional[str] = None
    bull_name: Optional[str] = None
    bull_register: Optional[str] = None
    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None

class InputDetailSchema(BaseModel):
    """Modelo para retornar resultados detallados de inputs con información de toro y cliente"""
    input_id: int
    quantity_received: float
    escalarilla: str
    status_id: str
    lote: str
    fv: datetime
    quantity_taken: float
    total: float
    created_at: datetime
    bull_name: str
    register_number: Optional[str]
    race_name: str
    client_name: str
    client_document: str
    
    class Config:
        orm_mode = True

class BullSchema(BaseModel):
    id: int
    name: str
    register_number: Optional[str] = Field(None, alias='register')
    race_name: Optional[str]
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class InputSchema(BaseSchema):
    quantity_received: float
    escalarilla: str
    bull_id: int
    status_id: InputStatus
    lote: str
    fv: datetime
    quantity_taken: float
    total: float
    user_id: int
    bull: Optional[BullSchema] = None
    
    class Config:
        orm_mode = True
        
    @classmethod
    def from_orm(cls, input_obj: "Input"):
        """Método personalizado para convertir de modelo ORM a Pydantic Schema"""
        if not input_obj:
            return None
            
        try:
            # Crear un diccionario con los datos del input
            input_dict = {
                "id": input_obj.id,
                "quantity_received": input_obj.quantity_received,
                "escalarilla": input_obj.escalarilla,
                "bull_id": input_obj.bull_id,
                "lote": input_obj.lote,
                "fv": input_obj.fv,
                "quantity_taken": input_obj.quantity_taken,
                "total": input_obj.total,
                "user_id": input_obj.user_id,
                "created_at": input_obj.created_at,
                "updated_at": input_obj.updated_at
            }
            
            # Convertir explícitamente el estado
            if hasattr(input_obj, "status_id") and input_obj.status_id:
                input_dict["status_id"] = InputStatus.from_model(input_obj.status_id)
            else:
                # Si no hay estado, usar 'pending' por defecto
                input_dict["status_id"] = InputStatus.pending
            
            # Agregar información del toro si está disponible
            if hasattr(input_obj, "bull") and input_obj.bull:
                input_dict["bull"] = {
                    "id": input_obj.bull.id,
                    "name": input_obj.bull.name,
                    "register": input_obj.bull.register,  # Esto usará el alias automáticamente
                    "race_name": input_obj.bull.race.name if input_obj.bull.race else None
                }
            
            # Crear el objeto esquema directamente desde el diccionario
            return cls(**input_dict)
        except Exception as e:
            # En caso de error, imprimir detalles y retornar None
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Error al convertir Input a InputSchema: {str(e)}")
            logger.error(f"Input: {input_obj.__dict__ if input_obj else None}")
            return None

class OutputBase(BaseModel):
    input_id: int
    quantity_output: float = Field(..., gt=0, description="Cantidad de salida - debe ser mayor que 0")
    remark: Optional[str] = None

class OutputCreate(BaseModel):
    quantity_output: float = Field(..., gt=0, description="Cantidad de salida - debe ser mayor que 0")
    output_date: Optional[datetime] = None
    remark: Optional[str] = None

class OutputUpdate(BaseModel):
    quantity_output: Optional[float] = Field(None, gt=0, description="Cantidad de salida - debe ser mayor que 0")
    output_date: Optional[datetime] = None
    remark: Optional[str] = None

class OutputSchema(BaseSchema):
    id: int
    input_id: int
    output_date: datetime
    quantity_output: float
    remark: Optional[str] = None
    
    class Config:
        orm_mode = True

class OutputDetailSchema(BaseModel):
    """Modelo para retornar resultados detallados de outputs con información del input asociado"""
    output_id: int
    input_id: int
    output_date: datetime
    quantity_output: float
    remark: Optional[str] = None
    escalarilla: str
    lote: str
    quantity_received: float
    bull_id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True 