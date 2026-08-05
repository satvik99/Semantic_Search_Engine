# Import the FastAPI framework (creates our web application)
from fastapi import FastAPI

# Import the router that contains upload-related endpoints
from app.routes.upload import router


# Create the FastAPI application object
# This is the entry point of our backend.
app = FastAPI()


# Register all routes present inside upload.py with the application.
# Without this, FastAPI would never know that /upload exists.
app.include_router(router)


# Root endpoint (GET /)
# Mainly used to verify that the server is running.
@app.get("/")
def home():
    return {"message": "Hello AI"}