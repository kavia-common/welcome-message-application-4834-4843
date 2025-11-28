from typing import Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# Configure application metadata for OpenAPI
app = FastAPI(
    title="Welcome Backend API",
    description="FastAPI backend that serves a welcome message and basic health check.",
    version="0.1.0",
    openapi_tags=[
        {"name": "Health", "description": "Endpoints for service health and readiness checks."},
        {"name": "Welcome", "description": "Endpoints that return welcome messages."},
    ],
)

# Keep CORS enabled as required
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this to known frontends via env
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class WelcomeResponse(BaseModel):
    """Response model for welcome endpoint."""
    message: str = Field(..., description="The welcome message to display.")


# PUBLIC_INTERFACE
@app.get("/", summary="Health Check", tags=["Health"])
def health_check() -> Dict[str, str]:
    """Basic health check endpoint.

    Returns:
        Dict[str, str]: A simple JSON payload indicating service health.
    """
    return {"message": "Healthy"}


# PUBLIC_INTERFACE
@app.get(
    "/api/welcome",
    response_model=WelcomeResponse,
    summary="Get Welcome Message",
    description="Returns a JSON object containing the welcome greeting.",
    tags=["Welcome"],
    operation_id="get_welcome_message",
)
def get_welcome() -> WelcomeResponse:
    """Return the welcome greeting.

    Returns:
        WelcomeResponse: JSON object with a 'message' field containing 'Welcome'.
    """
    return WelcomeResponse(message="Welcome")
