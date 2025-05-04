import pydantic
from typing import Annotated

Int8 = Annotated[int, pydantic.Field(ge=-128, le=127)] #b
Int16 = Annotated[int, pydantic.Field(ge=-32768, le=32767)] #h
Int32 = Annotated[int, pydantic.Field(ge=-2147483648, le=2147483647)] #i

UInt8 = Annotated[int, pydantic.Field(ge=0, le=255)] #B
UInt16 = Annotated[int, pydantic.Field(ge=0, le=65535)] #H
