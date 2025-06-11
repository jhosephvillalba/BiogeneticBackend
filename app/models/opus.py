from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.models.base_model import Base, BaseModel
from app.models.user import User
from app.models.bull import Bull
from datetime import date

class Opus(Base, BaseModel):
    __tablename__ = "opus"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    donante_id = Column(Integer, ForeignKey("bulls.id"), nullable=False)
    toro_id = Column(Integer, ForeignKey("bulls.id"), nullable=False)
    fecha = Column(Date, nullable=False)
    toro = Column(String(100), nullable=False)
    gi = Column(Integer, nullable=False)
    gii = Column(Integer, nullable=False)
    giii = Column(Integer, nullable=False)
    viables = Column(Integer, nullable=False)
    otros = Column(Integer, nullable=False)
    total_oocitos = Column(Integer, nullable=False)
    ctv = Column(Integer, nullable=False)
    clivados = Column(Integer, nullable=False)
    porcentaje_cliv = Column(String(10), nullable=False)
    prevision = Column(Integer, nullable=False)
    porcentaje_prevision = Column(String(10), nullable=False)
    empaque = Column(Integer, nullable=False)
    porcentaje_empaque = Column(String(10), nullable=False)
    vt_dt = Column(Integer, nullable=True)
    porcentaje_vtdt = Column(String(10), nullable=True)
    total_embriones = Column(Integer, nullable=False)
    porcentaje_total_embriones = Column(String(10), nullable=False)

    # Nuevos campos
    lugar = Column(String(100), nullable=True)
    finca = Column(String(100), nullable=True)

    # Relaciones
    cliente = relationship("User", back_populates="opus")
    donante = relationship("Bull", foreign_keys=[donante_id], back_populates="opus_donante")
    toro_rel = relationship("Bull", foreign_keys=[toro_id], back_populates="opus_toro")

    def __repr__(self):
        return f"<Opus(id={self.id}, cliente_id={self.cliente_id}, fecha={self.fecha})>"
