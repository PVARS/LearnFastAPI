from typing import Sequence

from app.features.user.domain.entities.user_entity import UserEntity
from app.features.user.domain.repository.user_repository import UserRepository
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.features.user.data.model.user import User
from sqlalchemy.exc import NoResultFound


class UserRepositoryImpl(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def find_all(self) -> Sequence[UserEntity]:
        query = select(User)
        try:
            users: Sequence[User] = self.session.execute(query).scalars().all()
        except NoResultFound:
            return []
        return [user.to_entity() for user in users]

    def find_by_email(self, email: str) -> UserEntity | None:
        query = select(User).filter_by(email=email)
        try:
            user: User = self.session.execute(query).scalar_one()
        except NoResultFound:
            return None
        return user.to_entity()
