from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.payment import calculate_total

app = FastAPI(title="Demo Payment Service", version="1.0.0")


class PaymentRequest(BaseModel):
    amount: float = Field(ge=0)
    tax_rate: float = Field(default=0.0, ge=0)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/payments/total")
def payment_total(request: PaymentRequest):
    try:
        total = calculate_total(request.amount, request.tax_rate)
        return {"amount": request.amount, "tax_rate": request.tax_rate, "total": total}
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
