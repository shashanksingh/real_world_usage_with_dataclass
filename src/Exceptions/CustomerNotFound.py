import dataclasses
from dataclasses import dataclass

from fastapi import HTTPException


@dataclass
class CustomerNotFound(HTTPException):
    headers: dict = dataclasses.field(default_factory=lambda: {"X-Error": "There goes my error"})
    status_code: int = 404
    detail: str = "Customer Not Found"
