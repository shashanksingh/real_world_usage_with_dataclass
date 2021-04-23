from dataclasses import dataclass

from pydantic.types import UUID


@dataclass
class CustomerResponseDTO:
    uuid: UUID
    name: str