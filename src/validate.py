from type_validate import ValidationResultType, Validator
from schema import userSchema
from type_schema import SchemaType
from type_validate import ValidateValueType

def validate(value: ValidateValueType, schema: SchemaType) -> ValidationResultType:
    validator = Validator()
    return {
        'result': validator.validate(value, schema),
        'message': validator.errors
    }

def validateUser(value: ValidateValueType):
    return validate(value, userSchema)