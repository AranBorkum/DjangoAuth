from abc import ABC, abstractmethod

from django_auth.core.use_cases.verify_user._types import VerifyUserOutputType


class VerifyUserOutputInterface(ABC):
    @property
    @abstractmethod
    def status(self) -> VerifyUserOutputType: ...

    @abstractmethod
    def finalize_verification(self) -> None: ...

    @abstractmethod
    def notify_verification_failure(self) -> None: ...
