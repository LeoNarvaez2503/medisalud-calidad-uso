from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from .database import Base

class Paciente(Base):
    __tablename__ = "pacientes"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    documento = Column(String(20), unique=True, index=True)
    historia_clinica = Column(String(50), unique=True, index=True)
    alergias = Column(Text, nullable=True) # Will fail to load selectively
    
    citas = relationship("Cita", back_populates="paciente")
    recetas = relationship("Receta", back_populates="paciente")

class Cita(Base):
    __tablename__ = "citas"
    
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))
    especialidad = Column(String(100), nullable=False)
    medico = Column(String(100), nullable=False)
    fecha_hora = Column(String(50), nullable=False)
    estado = Column(String(50), default="Pendiente")
    sede = Column(String(50), nullable=False)
    
    paciente = relationship("Paciente", back_populates="citas")

class Receta(Base):
    __tablename__ = "recetas"
    
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))
    medicamento = Column(String(100), nullable=False)
    dosis = Column(String(100), nullable=False)
    indicaciones = Column(Text, nullable=True)
    fecha = Column(DateTime, default=datetime.utcnow)
    
    paciente = relationship("Paciente", back_populates="recetas")

class IncidenteLog(Base):
    __tablename__ = "incidente_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, default=datetime.utcnow)
    modulo = Column(String(50), nullable=False)
    descripcion = Column(Text, nullable=False)
    rol_usuario = Column(String(50), nullable=False)
    sede = Column(String(50), nullable=False)
    caracteristica_iso_25022 = Column(String(50), nullable=False)
    justificacion_tecnica = Column(Text, nullable=False)
    violacion_rnf = Column(String(50), nullable=True)
