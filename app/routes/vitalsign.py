from app.database.models.default import ResponseModel, ErrorResponseModel
from app.database.vitalsign import get_vitalsign
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from fastapi_sqlalchemy import db


router = APIRouter()

headers = {"Access-Control-Allow-Origin": "*"}


@router.get("/{stay_id}", tags=["Data"], response_description="Data retrieved")
async def get_data(stay_id: int):
    data_dict = await get_vitalsign(stay_id, db)
    if data_dict:
        return ResponseModel(data_dict, "Data retrieved successfully", headers=headers)
    return ErrorResponseModel("An error occurred.", 404, "Data doesn't exist.")
