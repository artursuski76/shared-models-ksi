from datetime import datetime
from typing import Optional, List, Annotated, Union

from pydantic import Field

from models2.abase import BasicBasic
from models2.enums import TaskStatus
from models2.helpers.FlattenMixin import FlattenMixin
from models2.helpers.TaskTaskName import JpkVat7M, VatOss, WystawFakturyDlaZamowienWooCommerce, \
    PobierzZamowieniaWooCommerce
from models2.tasks.TaskError import TaskError

TaskName = Annotated[
    Union[
        JpkVat7M,
        VatOss,
        WystawFakturyDlaZamowienWooCommerce,
        PobierzZamowieniaWooCommerce
    ],
    Field(discriminator="task_name", alias="task_name", description="Rodzaj zadania"),
]


class Task(BasicBasic, FlattenMixin):
    __auto_id__ = False
    model_name: str = Field(
        "Task",
        title="Nazwa Modelu",
        json_schema_extra={"exclude_from_form": True}
    )

    my_id: str = Field(
        default="",
        title="Unikalny ID, np.: Abcde:PL789331",
        pattern=r"^[A-Za-z0-9]+(:[A-Za-z0-9]+)*$"
    )

    task_name: TaskName = Field(
        TaskName,
        title="Rodzaj zadania",
        json_schema_extra={"flatten": True}
    )

    status: TaskStatus = Field(
        TaskStatus.PENDING,
        json_schema_extra={"exclude_from_form": True}
    )

    executed_at: Optional[datetime] = Field(
        default=None,
        json_schema_extra={"exclude_from_form": True}
    )
    finished_at: Optional[datetime] = Field(
        default=None,
        json_schema_extra={"exclude_from_form": True}
    )

    processed_count: int = Field(default=0,
                                 json_schema_extra={"exclude_from_form": True}
                                 )
    error_count: int = Field(default=0,
                             json_schema_extra={"exclude_from_form": True}
                             )
    errors: List[TaskError] = Field(
        default_factory=list,
        json_schema_extra={"exclude_from_form": True}
    )
    updated_at: datetime = Field(default_factory=datetime.now, json_schema_extra={"exclude_from_form": True})


    class Couchbase:
        bucket = "Accounting"
        scope = "services"
        collection = "task"