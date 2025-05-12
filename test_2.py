from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Order(BaseModel):
    id: int
    items: list
    total_price: float

@app.post("/submit-order")
async def submit_order(request: Request):
    order_data = await request.json()
    order = Order(**order_data)

    if order.items == []:
        raise HTTPException(status=400, detail="Items list cannot be empty")

    if order.total_price <= 0:
        return {"error": "Total price must be greater than zero"}, 400

    return {"status": "ok"}
