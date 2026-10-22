from typing import Any, Union
from abc import ABC, abstractmethod

from app.messages.message_type import MessageType
from app.messages.base.base_message import BaseMessage, ContentPart


class MessageBaseFactory(ABC):
    """Abstract factory that defines the contract for creating BaseMessage instances.
    Subclasses implement create() to encapsulate the construction logic for each
    MessageType, keeping callers decoupled from the concrete message classes."""

    @abstractmethod
    def create(self, type: MessageType, 
        content: Union[str, list[ContentPart]], **kwargs: Any) -> BaseMessage:
        raise NotImplementedError("Must be implemented")
