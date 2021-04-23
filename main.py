from typing import List

from pydantic import ValidationError
from pydantic.types import UUID
from starlette.requests import Request
from starlette.responses import JSONResponse
from http import HTTPStatus
from src import Constants
from src.Dto.CustomerAddGiftCardRequestDTO import CustomerAddGiftCardRequestDTO
from src.Dto.CustomerAddGiftCardResponseDTO import CustomerAddGiftCardResponseDTO
from src.Dto.CustomerCreateRequestDTO import CustomerRequestDTO
from src.Dto.CustomerCreateResponseDTO import CustomerResponseDTO
from src.Domain.Customer import Customer
from src.Exceptions.CustomerNotFound import CustomerNotFound
from src.Exceptions.InvalidDiscount import InvalidDiscount
from fastapi import FastAPI

app = FastAPI()


@app.get("/giftcards")
async def get_giftcards():
    return Constants.ALL_GIFTCARDS


@app.post("/customer")
async def create_customer(customer_request: CustomerRequestDTO):
    customer = Customer(name=customer_request.name)
    Constants.ALL_CUSTOMERS[customer.uuid] = customer
    return CustomerResponseDTO(name=customer.name, uuid=customer.uuid)


@app.put("/customer/{customer_uuid}/giftcards")
async def add_giftcard_to_customer(customer_uuid: UUID, giftcard_uuids: CustomerAddGiftCardRequestDTO):
    giftcards = [Constants.ALL_GIFTCARDS_DICT.get(uuid) for uuid in giftcard_uuids.giftcard_uuids]
    try:
        customer = Constants.ALL_CUSTOMERS[customer_uuid]
        customer.add_gift_card(giftcards)
    except KeyError or AttributeError:
        raise CustomerNotFound()

    return CustomerAddGiftCardResponseDTO(giftcards=giftcards, customer=customer)


@app.exception_handler(InvalidDiscount)
async def unicorn_exception_handler(request: Request, exc: InvalidDiscount):
    return JSONResponse(
        status_code=HTTPStatus.BAD_REQUEST,
        content={"message": f"Oops! {exc} did something. There goes a rainbow..."},
    )


@app.exception_handler(CustomerNotFound)
async def unicorn_exception_handler(request: Request, exc: CustomerNotFound):
    return JSONResponse(
        status_code=HTTPStatus.NOT_FOUND,
        content={"message": f"Oops! {exc} did something. Customer Not Found"},
    )


@app.exception_handler(ValidationError)
async def unicorn_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=HTTPStatus.BAD_REQUEST,
        content={"message": f"Validation Error : {exc}"},
    )
