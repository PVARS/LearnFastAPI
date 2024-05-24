from app.core.repository.base_repository import BaseRepository
from app.features.user.domain.entities.user_entity import UserEntity
from abc import abstractmethod


class UserRepository(BaseRepository[UserEntity]):
    @abstractmethod
    def find_by_email(self, email: str) -> UserEntity | None:
        raise NotImplementedError()
