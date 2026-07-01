from fastapi import FastAPI

from sqlalchemy import select

from src.routers.api_router import main_page
from src.core.database import engine, Base, SessionDep
from src.models.tickets import TicketsModel



@main_page.post('/setup_database') 
async def setup_database(): 
    async with engine.begin() as conn: 
        await conn.run_sync(Base.metadata.drop_all) 
        await conn.run_sync(Base.metadata.create_all) 
        return {"success": True, "msg": "ok",}

@main_page.get("/")
async def get_lines(session: SessionDep):
    result = await session.execute(select(TicketsModel))
    tickets = result.scalars().all()
    return tickets
