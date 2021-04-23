# from dataclasses import dataclass
from pydantic.main import BaseModel
from pydantic.types import UUID


# @dataclass
class CustomerResponseDTO(BaseModel):
    uuid: UUID
    name: str