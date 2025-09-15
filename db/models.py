from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, Enum, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class Competition(Base):
    __tablename__ = "competitions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    picture_url = Column(String(500), nullable=True)
    prize_pool = Column(Integer, nullable=True)
    links = Column(JSON, nullable=True)
    date_start = Column(DateTime(timezone=True), nullable=False)
    date_end = Column(DateTime(timezone=True), nullable=True)
    type = Column(Enum("Hunt", "Tournament", "Bounty", name="event_type"), nullable=False)
    style = Column(Enum("RPG", "Dirt", "Ice", name="event_style"), nullable=True)
    style_custom = Column(String(50), nullable=True)  # only filled if user specifies another style
    platform_enum = Column(Enum("TrackMania 2020", "TMNF", name="event_platform_enum"), nullable=True)
    platform_custom = Column(String(100), nullable=True)
    recurring = Column(String(50), nullable=True)  # e.g., "weekly", "monthly", "3rd of month"
    approved = Column(Boolean, default=False)
    created_by = Column(Integer, nullable=False)
    alert = Column(String(200), nullable=True)
    lan_location = Column(String(200), nullable=True)  # e.g., "Paris LAN", blank if online
    region_lock = Column(String(200), nullable=True) # e.g., "Only for Romanian players"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), unique=True, nullable=False)  # Ubisoft login/username
    email = Column(String(200), unique=True, nullable=True)      # optional
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
