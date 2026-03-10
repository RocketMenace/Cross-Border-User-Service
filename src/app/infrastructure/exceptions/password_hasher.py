from app.infrastructure.exceptions.base import InfrastructureError


class PasswordHasherError(InfrastructureError):
    def __init__(self, *, message: str):
        self.message = message
        super().__init__()
