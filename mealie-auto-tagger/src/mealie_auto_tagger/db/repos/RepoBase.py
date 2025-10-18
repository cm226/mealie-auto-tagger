from sqlalchemy.orm import Session


class RepoBase():
    def __init__(
            self,
            session: Session
    ):
        self.session = session
