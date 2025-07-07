"""
Automation API – Gestione workflow, job, trigger e audit, standard singolare.
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

AUTOMATION_JOBS = {}

def get_current_user():
    return {"user_id": "admin"}

@router.get("/", response_model=List[AutomationJob])
def list_automation_jobs(skip: int = 0, limit: int = 100, current=Depends(get_current_user)):
    return list(AUTOMATION_JOBS.values())[skip:skip+limit]

@router.post("/", response_model=AutomationJob, status_code=status.HTTP_201_CREATED)
def create_automation_job(job: AutomationJob, current=Depends(get_current_user)):
    if job.id in AUTOMATION_JOBS:
        raise HTTPException(409, detail="Job already exists")
    AUTOMATION_JOBS[job.id] = job
    logging.info(f"[automation] Creato job {job.id} da {current['user_id']}")
    return job

@router.post("/trigger/{job_id}", status_code=status.HTTP_202_ACCEPTED)
def trigger_automation_job(job_id: str, current=Depends(get_current_user)):
    if job_id not in AUTOMATION_JOBS:
        raise HTTPException(404, detail="Job not found")
    logging.info(f"[automation] Trigger job {job_id} by {current['user_id']}")
    # Qui si può integrare la chiamata reale
    return {"status": "triggered", "job_id": job_id}

@router.delete("/{job_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_automation_job(job_id: str, current=Depends(get_current_user)):
    if job_id in AUTOMATION_JOBS:
        del AUTOMATION_JOBS[job_id]
        logging.info(f"[automation] Eliminato job {job_id} da {current['user_id']}")
