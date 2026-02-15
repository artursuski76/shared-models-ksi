from datetime import datetime
from typing import Optional, List

from pydantic import Field, model_validator

from models2.abase import BasicBasic
from models2.enums import TaskStatus, Year, Month
from models2.tasks.TaskError import TaskError


class TaskJpkCollect(BasicBasic):
    __auto_id__ = False

    model_name: str = Field(
        "TaskJpkVat7M",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )

    year: Year = Field(
        Year.Y_2025,
        title="Rok"
    )
    month: Month = Field(
        Month.M_1,
        title="Miesiąc"
    )

    my_id: Optional[str] = Field(
        default=None,
        title="Unikalny ID, np.: Abcde:PL789331",
        pattern=r"^[A-Za-z0-9]+(:[A-Z0-9][A-Za-z0-9]*)*$",
        json_schema_extra={"exclude_from_form": True}
    )

    task_name: str = Field(
        default="JpkVat7M",
        title="Rodzaj zadania"
    )

    status: TaskStatus = Field(
        TaskStatus.PENDING,
        json_schema_extra={"exclude_from_form": True}
    )

    executed_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None

    processed_count: int = 0
    error_count: int = 0

    errors: List[TaskError] = Field(
        default_factory=list,
        json_schema_extra={"exclude_from_form": True}
    )

    @model_validator(mode="after")
    def set_my_id(self) -> "TaskJpkCollect":
        if self.my_id:
            return self  # ktoś jawnie ustawił – szanujemy

        year = int(self.year.value if hasattr(self.year, "value") else self.year)
        month = int(self.month.value if hasattr(self.month, "value") else self.month)

        self.my_id = f"{year}:{month:02d}"
        return self


    class Couchbase:
        bucket = "Accounting"
        scope = "services"
        collection = "task"
