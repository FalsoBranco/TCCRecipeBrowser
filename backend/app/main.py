from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.routes.v1.api import api_router
from app.config import AppSettings, get_app_settings
from app.core.events import create_start_handler, create_stop_handler


def init_middleware(app: FastAPI, settings: AppSettings) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


# TODO: Implementar as exceptions
def register_exceptions(app: FastAPI) -> None:
    # app.add_exception_handler(HTTPException, http_error_handler)
    pass


def register_routers(app: FastAPI, settings: AppSettings) -> None:
    app.include_router(api_router, prefix=settings.API_PREFIX)


def get_application() -> FastAPI:
    settings: AppSettings = get_app_settings()
    application: FastAPI = FastAPI(**settings.fastapi_kwargs)

    init_middleware(app=application, settings=settings)

    register_exceptions(app=application)
    register_routers(app=application, settings=settings)

    application.add_event_handler(
        "startup",
        create_start_handler(application, settings),
    )
    application.add_event_handler(
        "shutdown",
        create_stop_handler(application),
    )

    return application


app: FastAPI = get_application()


# Update any base URLs or webhooks to use the public ngrok URL
