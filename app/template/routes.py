from fastapi import APIRouter, Request
from starlette import status

from app.template.services import template_service, get_service

router = APIRouter()


@router.post("/add_template/", status_code=status.HTTP_200_OK)
def add_template_service(payload: dict):
    template_service(payload)
    return payload


@router.post("/get_form/", status_code=status.HTTP_200_OK)
def get_form_service(request: Request):
    return get_service(request.query_params)
