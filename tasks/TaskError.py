from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TaskError(BaseModel):
    timestamp: datetime
    message: str
    record_id: Optional[str] = None