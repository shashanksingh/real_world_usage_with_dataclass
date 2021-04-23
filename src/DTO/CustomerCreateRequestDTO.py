from pydantic import BaseModel


class CustomerRequestDTO(BaseModel):
    name: str
