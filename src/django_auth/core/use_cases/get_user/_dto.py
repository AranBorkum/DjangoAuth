from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class GetUserDTO:
    user_id: UUID
