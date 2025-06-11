from typing import Optional, TYPE_CHECKING
from pydantic import BaseModel, Field
from app.schemas.base_schema import BaseSchema
from enum import Enum
from app.models.bull import BullStatus as ModelBullStatus
from datetime import datetime

if TYPE_CHECKING:
    from app.models.bull import Bull

class RaceSchema(BaseSchema):
    name: str
    description: str
    code: str

class RaceCreate(BaseModel):
    name: str
    description: str
    code: str

class SexSchema(BaseSchema):
    name: str
    code: int

class SexCreate(BaseModel):
    name: str
    code: int

class BullStatus(str, Enum):
    active = "Active"
    inactive = "Inactive"
    
    @classmethod
    def from_model(cls, status: ModelBullStatus) -> "BullStatus":
        """Convierte de estado del modelo a estado del esquema"""
        if status == ModelBullStatus.active:
            return cls.active
        elif status == ModelBullStatus.inactive:
            return cls.inactive
        return None
        
    def to_model(self) -> ModelBullStatus:
        """Convierte de estado del esquema a estado del modelo"""
        if self == BullStatus.active:
            return ModelBullStatus.active
        elif self == BullStatus.inactive:
            return ModelBullStatus.inactive
        return None

class BullBase(BaseModel):
    name: str
    registration_number: Optional[str] = Field(None, alias="register")
    race_id: int
    sex_id: int
    status: Optional[BullStatus] = BullStatus.active

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            BullStatus: lambda v: v.value if v else None
        }

class BullCreate(BullBase):
    pass

class BullUpdate(BullBase):
    name: Optional[str] = None
    registration_number: Optional[str] = Field(None, alias="register")
    race_id: Optional[int] = None
    sex_id: Optional[int] = None
    status: Optional[BullStatus] = None

class BullSchema(BaseSchema, BullBase):
    user_id: int
    
    class Config:
        orm_mode = True
        
    @classmethod
    def from_orm(cls, bull: "Bull"):
        """Método personalizado para convertir de modelo ORM a Pydantic Schema"""
        if not bull:
            return None
        
        try:
            # Crear un diccionario con los datos del bull
            bull_dict = {
                "id": bull.id,
                "name": bull.name,
                "register": bull.register,
                "race_id": bull.race_id,
                "sex_id": bull.sex_id,
                "user_id": bull.user_id,
                "created_at": bull.created_at,
                "updated_at": bull.updated_at
            }
            
            # Convertir explícitamente el estado
            if hasattr(bull, "status") and bull.status:
                if bull.status == ModelBullStatus.active:
                    bull_dict["status"] = BullStatus.active
                elif bull.status == ModelBullStatus.inactive:
                    bull_dict["status"] = BullStatus.inactive
                else:
                    # En caso de un estado desconocido, usar 'active' por defecto
                    bull_dict["status"] = BullStatus.active
            else:
                # Si no hay estado, usar 'active' por defecto
                bull_dict["status"] = BullStatus.active
            
            # Crear el objeto esquema directamente desde el diccionario
            return cls(**bull_dict)
        except Exception as e:
            # En caso de error, imprimir detalles y retornar None
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Error al convertir Bull a BullSchema: {str(e)}")
            logger.error(f"Bull: {bull.__dict__ if bull else None}")
            return None 

class UserInfoSchema(BaseModel):
    id: int
    full_name: str
    email: str
    number_document: str
    phone: str
    type_document: Optional[str] = None
    specialty: Optional[str] = None

class BullDetailSchema(BaseModel):
    id: int
    name: str
    registration_number: Optional[str] = Field(None, alias="register")
    race_id: int
    race_name: Optional[str] = None
    sex_id: int
    sex_name: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    user: UserInfoSchema
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat() if v else None
        } 