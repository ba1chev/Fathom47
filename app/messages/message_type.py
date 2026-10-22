from enum import Enum


class MessageType(Enum):
    HUMAN_MESSAGE = "human"
    SYSTEM_MESSAGE = "system"
    AI_MESSAGE = "ai"
    TOOL_MESSAGE = "tool"
