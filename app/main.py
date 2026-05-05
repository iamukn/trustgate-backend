from fastapi import FastAPI
from api.v1.routes.trust_gate import router as trust_gate_router
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "*"
]

# API app instance
app = FastAPI(title="TrustGate API")

# add cors middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Specify allowed origins
    allow_credentials=True, # Allow cookies and credentials
    allow_methods=["*"], # Allow all HTTP methods
    allow_headers=["*"], # Allow all headers
)

# register the trustGate router
app.include_router(trust_gate_router)
