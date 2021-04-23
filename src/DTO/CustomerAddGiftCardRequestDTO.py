from typing import List

from pydantic import BaseModel
from pydantic.types import UUID


class CustomerAddGiftCardRequestDTO(BaseModel):
    giftcard_uuids: List[UUID]
