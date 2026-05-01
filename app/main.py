from fastapi import FastAPI
from api.v1.routes.trust_gate import router as trust_gate_router

# API app instance
app = FastAPI(title="TrustGate API")

# register the trustGate router
app.include_router(trust_gate_router)
