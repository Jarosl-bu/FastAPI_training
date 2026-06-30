from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.database import Base



class TicketsModel(Base): 
    __tablename__ = 'tickets' 

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped(str)
    place: Mapped(int)