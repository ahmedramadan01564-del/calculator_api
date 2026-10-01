from pydantic import BaseModel

class CalculationRequest(BaseModel):
    """The JSON body a client sends to POST /calculate."""
    a: float
    b: float
    operation: str

class CalculationResponse(BaseModel):
    """The JSON body your API sends back."""
    result: float    

class HealthResponse(BaseModel):
    """The JSON body returned by GET /health"""
    status: str