import uuid

import dataclasses
from pydantic.dataclasses import dataclass


@dataclass
class Product:
    # uuid: str = dataclasses.field(default_factory=lambda: uuid.uuid4())
    name: str
