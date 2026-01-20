from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Email Assistant API",
    description="AI-powered email assistant backend",
    version="0.1.0",
)

# CORS configuration for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


# Routers will be added here as we implement them
# from app.routers import auth, emails
# app.include_router(auth.router, prefix="/auth", tags=["auth"])
# app.include_router(emails.router, prefix="/emails", tags=["emails"])
