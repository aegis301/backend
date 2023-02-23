from .models.mimic_derived.Vitalsign import Vitalsign
from .schemas.mimic_derived.Vitalsign import VitalsignBase
from sqlalchemy.orm import Session


async def get_vitalsign(stay_id: int, db: Session):
    """Get data from database"""
    data = db.session.query(Vitalsign).filter(Vitalsign.stay_id == stay_id).all()
    if data:
        return vitalsign_helper(data)
    else:
        return None


def vitalsign_helper(data: Vitalsign) -> VitalsignBase:
    """Helper function to convert data to dict of lists."""
    out_data = {
        "subject_id": None,
        "stay_id": None,
        "charttime": [],
        "heart_rate": [],
        "sbp": [],
        "dbp": [],
        "mbp": [],
        "sbp_ni": [],
        "dbp_ni": [],
        "mbp_ni": [],
        "resp_rate": [],
        "temperature": [],
        "temperature_site": [],
        "spo2": [],
        "glucose": [],
    }
    for point in data:
        out_data["subject_id"] = point.subject_id
        out_data["stay_id"] = point.stay_id
        out_data["charttime"].append(point.charttime)
        out_data["heart_rate"].append(point.heart_rate)
        out_data["sbp"].append(point.sbp)
        out_data["dbp"].append(point.dbp)
        out_data["mbp"].append(point.mbp)
        out_data["sbp_ni"].append(point.sbp_ni)
        out_data["dbp_ni"].append(point.dbp_ni)
        out_data["mbp_ni"].append(point.mbp_ni)
        out_data["resp_rate"].append(point.resp_rate)
        out_data["temperature"].append(point.temperature)
        out_data["temperature_site"].append(point.temperature_site)
        out_data["spo2"].append(point.spo2)
        out_data["glucose"].append(point.glucose)

    return out_data
