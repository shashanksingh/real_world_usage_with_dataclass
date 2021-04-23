from typing import List
from pydantic import BaseModel

from src.Domain.Customer import Customer
from src.Domain.Giftcard import Giftcard


class CustomerAddGiftCardResponseDTO(BaseModel):
    giftcards: List[Giftcard]
    customer: Customer
