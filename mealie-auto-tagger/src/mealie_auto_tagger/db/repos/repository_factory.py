from functools import cached_property
from sqlalchemy.orm import Session

from .LabelRepo import LabelRepo
from .ListItemRepo import ListItemRepo


class AllRepositories:

    def __init__(
        self,
        session: Session
    ) -> None:
        self.session = session

    @cached_property
    def labelRepo(self) -> LabelRepo:
        return LabelRepo(self.session)

    @cached_property
    def listItemRepo(self) -> ListItemRepo:
        return ListItemRepo(self.session)
