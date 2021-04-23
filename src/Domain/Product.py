import uuid

import dataclasses
from typing import Optional
from pydantic.dataclasses import dataclass


@dataclass
class Product:
    # uuid: Optional[str] = dataclasses.field(default_factory=lambda: str(uuid.uuid1()))
    name: str
