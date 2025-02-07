from ninja import NinjaAPI
from .models import Job
from django.shortcuts import get_object_or_404
from pydantic import BaseModel

api = NinjaAPI()

class JobSchema(BaseModel):
    title: str
    company: str
    location: str
    description: str
    salary: float | None = None

@api.get("/jobs")
def list_jobs(request):
    jobs = Job.objects.all().values()
    return list(jobs)

@api.post("/jobs")
def create_job(request, payload: JobSchema):
    job = Job.objects.create(**payload.dict())
    return {"id": job.id, "message": "Job created successfully"}

@api.get("/jobs/{job_id}")
def get_job(request, job_id: int):
    job = get_object_or_404(Job, id=job_id)
    return {
        "id": job.id,
        "title": job.title,
        "company": job.company,
        "location": job.location,
        "description": job.description,
        "salary": job.salary,
    }

@api.delete("/jobs/{job_id}")
def delete_job(request, job_id: int):
    job = get_object_or_404(Job, id=job_id)
    job.delete()
    return {"message": "Job deleted successfully"}
