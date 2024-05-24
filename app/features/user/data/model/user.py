from app.core.model.model import Base
from sqlalchemy.orm import Mapped
from sqlalchemy import Column, String, Boolean
from app.features.user.domain.entities.user_entity import UserEntity


class User(Base):
    __tablename__ = "users"

    email: Mapped[str] = Column(String(255))
    username: Mapped[str] = Column(String(50))
    status: Mapped[bool] = Column(Boolean, default=False)
    password: Mapped[str] = Column(String(255), nullable=True)

    def to_entity(self) -> UserEntity:
        return UserEntity(
            id=self.id_,
            email=self.email,
            username=self.username,
            status=self.status,
            password=self.password,
            created_at=self.created_at,
            updated_at=self.updated_at,
            is_deleted=self.is_deleted
            # created_at=self.created_at,
            # creator_name=self.creator_name,
            # updated_at=self.updated_at,
            # updater_name=self.updater_name,
            # deleted_at=self.deleted_at,
        )
