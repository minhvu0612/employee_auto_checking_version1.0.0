# Checking v1.0.0
from fastapi import APIRouter
from fastapi.responses import JSONResponse
import numpy as np
from PIL import Image

# Module training
from training.src.make_data_train import Trainer
from training.src.face_rec import Face_recognition

# Package
from ...core.schemas.v1.schema import *
from ...helpers.base64_convert import *
from ...mocks.response import *
from ...helpers.exception_handler import ExceptionType

# Init recognization
face_recogny = Face_recognition()

# Init router and operation
router = APIRouter(
    prefix="/eac-ai/api/v1/checking",
    tags=["EAC-AI"],
    dependencies=[],
    responses={},
)


@router.post("/user")
async def add_new_member(item: Member):
    '''add user router'''
    trainer = Trainer()
    img = stringToRGB(item.image)
    trainer.add_member(image = img, name = item.name)
    response = ExceptionType(200, "Success", data = data).getResponse()
    return JSONResponse(status_code = 200, content = response)


@router.delete("/user")
async def delete_member(item: Emiliation):
    '''delete user router'''
    response = ExceptionType(200, "Success", data = data).getResponse()
    return JSONResponse(status_code = 200, content = response)


@router.post("/")
async def checking(item: Detection):
    '''recogny user router'''
    image = stringToRGB(item.image)
    result = face_recogny.recogny_face(image)
    if result == None:
        response = ExceptionType(400, "Bad Request", error = error).getResponse()
        return JSONResponse(status_code = 400, content = response)
    frame, bbox, name, current_time = result
    frame_b64 = RGB2String(result[0])
    if name == "Unknown":
        response = ExceptionType(400, "Bad Request", error = error).getResponse()
        return JSONResponse(status_code = 400, content = response)
    else:
        response = ExceptionType(200, "Success", data = data(name)).getResponse()
        return JSONResponse(status_code = 200, content = response)