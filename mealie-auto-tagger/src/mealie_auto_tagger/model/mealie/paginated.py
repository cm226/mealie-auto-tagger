from typing import Generic, Optional, TypeVar
from pydantic import BaseModel

T = TypeVar("T")

class PaginatedQueryResp(BaseModel, Generic[T]):
  page: int
  per_page: int
  total: int
  total_pages: int
  items: list[T]
  next: Optional[str]
  previous: Optional[str]