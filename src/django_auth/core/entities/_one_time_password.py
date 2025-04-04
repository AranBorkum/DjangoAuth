from datetime import datetime
from uuid import UUID


class OneTimePassword:
    def __init__(
        self,
        one_time_password: str,
        user_id: UUID,
        created_at: datetime,
    ) -> None:
        self.one_time_password = one_time_password
        self.user_id = user_id
        self.created_at = created_at
