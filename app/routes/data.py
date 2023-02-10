from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from app.database.data import get_data
from app.database.models.default import ResponseModel

router = APIRouter()

headers = {"Access-Control-Allow-Origin": "*"}


@router.get("/data/{patient_id}/{item_id}", tags=["Data"], headers=headers)
async def get_data():
    return {"data": data_dict}
