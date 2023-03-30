# Schema v1.0.0
from pydantic import BaseModel
from typing import Union

# Class 
class Member(BaseModel):
    email: str
    image: str

class Detection(BaseModel):
    image: str
    checking_type: str

class Emiliation(BaseModel):
    email: str