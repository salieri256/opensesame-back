class ExtendedException(Exception):
    pretext = ''
    def __init__(self, message: str, *args: object) -> None:
        if self.pretext:
            message = f'{self.pretext}: {message}'
        super().__init__(message, *args)

class SqlSyntaxException(ExtendedException):
    pretext = 'SQL_SYNTAX_EXCEPTION'

class UserNotFoundException(ExtendedException):
    pretext = 'SQL_BUG_EXCEPTION'

class NfcNotFoundException(ExtendedException):
    pretext = 'SQL_BUG_EXCEPTION'

class EnterLogNotFoundException(ExtendedException):
    pretext = 'SQL_BUG_EXCEPTION'