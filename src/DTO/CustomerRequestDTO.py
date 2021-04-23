from dataclasses import dataclass

from pydantic.types import UUID
from pydantic import BaseModel

@dataclass
class CustomerRequestDTO(BaseModel):
    name: str