from pydantic import Field
from typing import Literal, Optional

from app.messages.message_type import MessageType
from app.messages.usage_metadata import UsageMetadata
from app.messages.base.base_message import BaseMessage
from app.messages.tool_calls.tool_call import ToolCall
from app.messages.tool_calls.invalid_tool_call import InvalidToolCall


class AIMessage(BaseMessage):
    """Represents the model's response to one or more preceding human or tool turns.
    In addition to the generated text, it carries any tool invocations the model decided
    to make (tool_calls), any that could not be parsed (invalid_tool_calls), and token
    usage statistics (usage_metadata). When the model replies with plain text only,
    tool_calls and invalid_tool_calls are empty lists."""
    type: Literal[MessageType.AI_MESSAGE] = MessageType.AI_MESSAGE
    tool_calls: list[ToolCall] = Field(
        default_factory = list,
        description = "Structured tool invocations the model decided to make. Each entry is a "
            "fully parsed ToolCall with a name, validated arguments, and an ID the corresponding "
            "ToolMessage must echo back. Empty when the model replied with plain text."
    )
    invalid_tool_calls: list[InvalidToolCall] = Field(
        default_factory = list,
        description = "Tool invocations the model attempted but that could not be parsed or "
            "validated — e.g. malformed JSON arguments or an unknown tool name. Kept separate "
            "so the application can decide whether to retry, fall back, or surface the error."
    )
    usage_metadata: Optional[UsageMetadata] = Field(
        default = None,
        description = "Token consumption for this response as reported by the model server. "
            "Use this to track costs, enforce budget limits, or feed monitoring dashboards. "
            "None when the provider did not return usage information."
    )

    def __str__(self) -> str:
        body = self.content if isinstance(self.content, str) else str(self.content)
        return f"AI: {body}"
