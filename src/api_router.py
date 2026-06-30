from fastapi import APIRouter



main_page = APIRouter(prefix="/main")
auth = APIRouter(prefix="/auth")
buy_ticket = APIRouter(prefix="/tickets")

api_router = APIRouter()

api_router.include_router(main_page)
api_router.include_router(auth)
api_router.include_router(buy_ticket)