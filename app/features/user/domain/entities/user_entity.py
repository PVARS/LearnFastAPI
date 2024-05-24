import uuid
from datetime import datetime


class UserEntity(object):
    def __init__(
            self,
            id: uuid,
            email: str,
            username: str,
            status: bool,
            created_at: datetime,
            updated_at: datetime,
            is_deleted: bool,
            password: str | None = None,
    ):
        self.id = id
        self.email = email
        self.username = username
        self.password = password
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_deleted = is_deleted
