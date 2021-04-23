from typing import List

from src import Constants
from src.Customer import Customer
from src.Giftcard import Giftcard
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
    except  Exception ex:
        return ex.to_s
    return customer

