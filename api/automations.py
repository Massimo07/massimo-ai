"""
Automations API – Gestione workflow, job, trigger e audit, variante plurale.
(Usa questa solo se vuoi la versione “compatibile” con plural naming.)
"""

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List
import logging

router = APIRouter()

class AutomationJob(BaseModel):
    id: str
    name: str
    status: str

AUTOMATIONS = {}

def get_current_user():
    return {"user_id": "admin"}

@router.get("/", response_model=List[AutomationJob])
def list_automations(skip: int = 0, limit: int = 100, current=Depends(get_current_user)):
    return list(AUTOMATIONS.values())[skip:skip+limit]

@router.post("/", response_model=AutomationJob, status_code=status.HTTP_201_CREATED)
def create_automation(job: AutomationJob, current=Depends(get_current_user)):
    if job.id in AUTOMATIONS:
        raise HTTPException(409, detail="Job already exists")
    AUTOMATIONS[job.id] = job
    logging.info(f"[automations] Creato job {job.id} da {current['user_id']}")
    return job

@router.post("/trigger/{job_id}", status_code=status.HTTP_202_ACCEPTED)
def trigger_automation(job_id: str, current=Depends(get_current_user)):
    if job_id not in AUTOMATIONS:
        raise HTTPException(404, detail="Job not found")
    logging.info(f"[automations] Trigger job {job_id} by {current['user_id']}")
    return {"status": "triggered", "job_id": job_id}

@router.delete("/{job_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_automation(job_id: str, current=Depends(get_current_user)):
    if job_id in AUTOMATIONS:
        del AUTOMATIONS[job_id]
        logging.info(f"[automations] Eliminato job {job_id} da {current['user_id']}")
