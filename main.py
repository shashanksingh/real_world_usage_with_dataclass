from typing import List

from pydantic.types import UUID
from starlette.requests import Request
from starlette.responses import JSONResponse
from http import HTTPStatus
from src import Constants
from src.DTO.CustomerRequestDTO import CustomerRequestDTO
from src.DTO.CustomerResponseDTO import CustomerResponseDTO
from src.Domain.Customer import Customer
from src.Exceptions.CustomerNotFound import CustomerNotFound
from src.Exceptions.InvalidDiscount import InvalidDiscount
from src.Domain.Giftcard import Giftcard
from fastapi import FastAPI

app = FastAPI()


@app.get("/giftcards")
async def get_giftcards():
    return Constants.ALL_GIFTCARDS


@app.post("/customer")
async def create_customer(customer_data : CustomerRequestDTO):
    customer = Customer(name=CustomerRequestDTO.name)
    Constants.ALL_CUSTOMERS[customer.uuid] = customer
    return CustomerResponseDTO(name = customer.name, uuid = customer.uuid)


@app.put("/customer/{uuid}/giftcards")
async def add_giftcard_to_customer(uuid: UUID, giftcards: List[Giftcard]):
    customer = Constants.ALL_CUSTOMERS.get(uuid)
    customer.add_gift_card(giftcards)
    return customer


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
