from typing import Any, Literal, TypedDict

class SchemaPropertyType(TypedDict, total=False):
    type: Literal['boolean', 'binary', 'date', 'datetime', 'dict', 'float', 'integer', 'list', 'number', 'set', 'string']
    required: bool
    empty: bool
    schema: 'SchemaPropertyType'

SchemaType = dict[Any, SchemaPropertyType]