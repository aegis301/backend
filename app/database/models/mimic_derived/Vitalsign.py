from sqlalchemy import Column, Integer, String, DateTime

from ....db import Base


class Vitalsign(Base):
    __tablename__ = "vitalsign"
    __table_args__ = {"schema": "mimiciv_derived"}

    subject_id = Column(Integer, primary_key=True, index=True)
    stay_id = Column(Integer, primary_key=True, index=True)
    charttime = Column(DateTime, primary_key=True, index=True)
    heart_rate = Column(Integer)
    sbp = Column(Integer)
    dbp = Column(Integer)
    mbp = Column(Integer)
    sbp_ni = Column(Integer)
    dbp_ni = Column(Integer)
    mbp_ni = Column(Integer)
    resp_rate = Column(Integer)
    temperature = Column(Integer)
    temperature_site = Column(String)
    spo2 = Column(Integer)
    glucose = Column(Integer)
