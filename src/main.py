from datetime import datetime, UTC

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.requests import Request

from src.routers.api_router import api_router
from src.core.logger import logger



def create_app():
    app = FastAPI(
        title = "Theatre"
    )
    app.include_router(api_router)

    return app

app = create_app()



@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.detail,
            "path": request.url.path,
            "timestamp": datetime.now(UTC).isoformat(),
        },
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unexpected error: {str(exc)}")

    return JSONResponse(
        status_code=500,
        content={
            "detail": "An unexpected error occurred",
            "path": request.url.path,
        },
    )


@app.get("/", tags=["Root"])
async def root():
    return RedirectResponse("/docs")