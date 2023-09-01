from abc import abstractmethod, ABC
from typing import Any, Iterable, List, Mapping, Optional

from airbyte_cdk.models import SyncMode


class PartitionGenerator(ABC):
    @abstractmethod
    def generate_partitions(self, sync_mode: SyncMode, cursor_field: Optional[List[str]]) -> Iterable[Optional[Mapping[str, Any]]]:
        pass
