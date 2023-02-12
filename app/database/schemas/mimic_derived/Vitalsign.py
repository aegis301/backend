from pydantic import BaseModel
from datetime import datetime


class VitalsignBase(BaseModel):
    subject_id: int
    stay_id: int
    charttime: list[datetime]
    heart_rate: list[int]
    sbp: list[int]
    dbp: list[int]
    mbp: list[int]
    sbp_ni: list[int]
    dbp_ni: list[int]
    mbp_ni: list[int]
    resp_rate: list[int]
    temperature: list[int]
    temperature_site: list[str]
    spo2: list[int]
    glucose: list[int]

    class Config:
        orm_mode = True
