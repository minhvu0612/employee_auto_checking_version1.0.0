# api.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Packages
from .v1.checking import router
from ..helpers.exception_handler import exception_types

# Settings
from ..core.settings import *

# Init application
app = FastAPI(exception_handlers = exception_types)

# Cors-header-origin
app.add_middleware(
    CORSMiddleware,
    allow_origins = ORIGINS,
    allow_credentials = CREDENTIALS,
    allow_methods = METHODS,
    allow_headers = HEADERS,
)

# Add router cluster
app.include_router(router)