from fastapi import FastAPI, HTTPException
from models import CalculationRequest,HealthResponse,CalculationResponse
from calculator.operations import OPERATIONS

app = FastAPI(title = "Calculator API")

calculation_history = []

@app.get("/health",response_model=HealthResponse )
def health():
    """Report that the service is runing."""

    return HealthResponse(status = "ok")

@app.post("/calculate",response_model=CalculationResponse)
def calculat(request : CalculationRequest):
    """Perform one calculation and return the result."""

    operation_function = OPERATIONS.get(request.operation)

    if operation_function is None:
        raise HTTPException(
            status_code=400,
            detail=f"Operation '{request.operation}' was not recognised",
        )
    try:
        result = operation_function(request.a,request.b)
    except ZeroDivisionError:
         raise HTTPException(
            status_code=400,
            detail="Cannot divide by zero.",
        )

    calculation_history.append({
       "a": request.a,
       "b": request.b,
       "operation": request.operation,
       "result": result,

    })

    return CalculationResponse(result=result)

@app.get("/history")
def history(limit: int = 10):
    return calculation_history[-limit:]