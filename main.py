from typing import List

from starlette.requests import Request
from starlette.responses import JSONResponse
from http import HTTPStatus
from src import Constants
from src.Domain.Customer import Customer
from src.Exceptions.CustomerNotFound import CustomerNotFound
from src.Exceptions.InvalidDiscount import InvalidDiscount
from src.Domain.Giftcard import Giftcard
from fastapi import FastAPI

app = FastAPI()


@app.get("/giftcards")
def get_giftcards():
    return Constants.ALL_GIFTCARDS


@app.post("/customer")
def create_customer(name: str):
    return Customer(name=name)


@app.put("/customer/{uuid}/giftcards")
def add_giftcard_to_customer(uuid: int, giftcards: List[Giftcard]):
    customer = Constants.ALL_CUSTOMERS.get(uuid)
    try:
        customer.add_gift_card(giftcards)
    except Exception:
        raise CustomerNotFound()
    return customer


@app.exception_handler(InvalidDiscount)
async def unicorn_exception_handler(request: Request, exc: InvalidDiscount):
    return JSONResponse(
        status_code=HTTPStatus.BAD_REQUEST,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


@app.exception_handler(CustomerNotFound)
async def unicorn_exception_handler(request: Request, exc: CustomerNotFound):
    return JSONResponse(
        status_code=HTTPStatus.NOT_FOUND,
        content={"message": f"Oops! {exc.name} did something. Customer Not Found"},
    )
