from typing import Union, Callable, Optional, TypedDict
from cerberus.validator import Validator as OriginalValidator
from type_schema import SchemaType

ValidateValueType = Union[dict, list]

class ValidationResultType(TypedDict):
    result: bool
    message: dict

class Validator(OriginalValidator):
    validate: Callable[[ ValidateValueType, Optional[SchemaType] ], bool]
    schema: SchemaType
    errors: dict