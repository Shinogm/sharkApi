from pydantic import BaseModel
from typing import Annotated
from fastapi import Form

class Client(BaseModel):
    name: str
    last_name: str
    phone: str
    email: str | None = None

    @classmethod
    def as_form(
        cls,
        name: Annotated[str, Form(...)],
        last_name: Annotated[str, Form(...)],
        phone: Annotated[str, Form(...)],
        email: Annotated[str | None, Form(...)] = None
    ):
        return cls(
            name=name,
            last_name=last_name,
            phone=phone,
            email=email
        )

class ModifyClient(BaseModel):
    name: str | None = None
    last_name: str | None = None
    phone: str | None = None
    email: str | None = None

    @classmethod
    def as_form(
        cls,
        name: Annotated[str | None, Form(...)] = None,
        last_name: Annotated[str | None, Form(...)] = None,
        phone: Annotated[str | None, Form(...)] = None,
        email: Annotated[str | None, Form(...)] = None
    ):
        return cls(
            name=name,
            last_name=last_name,
            phone=phone,
            email=email
        )