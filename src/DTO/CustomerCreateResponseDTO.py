from pydantic.main import BaseModel
from pydantic.types import UUID


class CustomerResponseDTO(BaseModel):
    uuid: UUID
    name: str