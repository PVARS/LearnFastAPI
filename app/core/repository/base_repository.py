from abc import ABC, abstractmethod
from typing import TypeVar, Sequence, Generic

_T = TypeVar('_T')


class BaseRepository(ABC, Generic[_T]):
    @abstractmethod
    def find_all(self) -> Sequence[_T]:
        raise NotImplementedError()
