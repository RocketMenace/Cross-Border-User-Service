from app.domain.exceptions.base import DomainError


class InvalidMiddleNameNameError(DomainError):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)
