from type_schema import SchemaType

userSchema: SchemaType = {
    'name': {
        'type': 'string',
        'required': True,
        'empty': False,
    },
    'nfcIdList': {
        'type': 'list',
        'required': True,
        'empty': True,
        'schema': {
            'type': 'string',
            'empty': False
        },
    }
}