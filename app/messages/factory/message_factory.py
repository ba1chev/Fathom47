from typing import Any, Union

from app.messages.ai_message import AIMessage
from app.messages.message_type import MessageType
from app.messages.tool_message import ToolMessage
from app.messages.human_message import HumanMessage
from app.messages.system_message import SystemMessage
from app.messages.base.base_message import BaseMessage, ContentPart
from app.messages.factory.message_base_factory import MessageBaseFactory


class MessageFactory(MessageBaseFactory):
    """Concrete factory that maps each MessageType to its corresponding BaseMessage
    subclass and delegates construction to it. Additional keyword arguments are
    forwarded verbatim, so callers can supply message-specific fields such as
    tool_call_id for ToolMessage or example for HumanMessage without the factory
    needing to know about them explicitly."""

    _registry: dict[MessageType, type[BaseMessage]] = {
        MessageType.HUMAN_MESSAGE: HumanMessage,
        MessageType.SYSTEM_MESSAGE: SystemMessage,
        MessageType.AI_MESSAGE: AIMessage,
        MessageType.TOOL_MESSAGE: ToolMessage
    }

    def create(self, type: MessageType, 
        content: Union[str, list[ContentPart]],**kwargs: Any) -> BaseMessage:
        cls = self._registry.get(type)

        if cls is None:
            raise ValueError(
                f"No message class registered for type '{type}'. "
                f"Known types: {list(self._registry)}"
            )

        return cls(content=content, **kwargs)
