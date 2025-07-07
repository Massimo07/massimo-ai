# api/ai.py
from fastapi import APIRouter, Depends
from core.security import validate_token
from ai_engine.pipeline import predict

router = APIRouter()

@router.post("/predict")
def ai_predict_route(input_data: dict, token: str = Depends(validate_token)):
    res = predict(input_data, model_name=input_data.get("model", "gpt-4o"))
    return res
