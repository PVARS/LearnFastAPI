from sqlalchemy.orm import Mapped
from sqlalchemy import Column, TIMESTAMP, Integer, func, Boolean
from datetime import datetime
from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class Base(object):
    id_: Mapped[int] = Column(Integer, primary_key=True, index=True)
    created_at: Mapped[datetime] = Column(TIMESTAMP, server_default=func.now())
    updated_at: Mapped[datetime] = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.current_timestamp()
    )
    is_deleted: Mapped[bool] = Column(Boolean, default=False)
