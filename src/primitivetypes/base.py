from abc import ABC, abstractmethod
from typing import Any, Generic, Literal, NotRequired, TypedDict, TypeVar


Number = TypeVar("Number", int, float)
TypeString = Literal["INT", "FLOAT", "STRING"]


class NumberInputDict(TypedDict, Generic[Number]):
    default: Number
    min: NotRequired[Number]
    max: NotRequired[Number]
    step: Number
    display: Literal["number", "slider"]


class StringInputDict(TypedDict):
    default: str
    multiline: bool


class InputDict(TypedDict):
    required: dict[
        str,
        (
            tuple[TypeString | list[TypeString]] |
            tuple[TypeString, NumberInputDict[int] | NumberInputDict[float] | StringInputDict]
        )
    ]

    hidden: NotRequired[dict[
        str,
        (
            tuple[TypeString | list[TypeString]] |
            tuple[TypeString, NumberInputDict[int] | NumberInputDict[float] | StringInputDict]
        )
    ]]

    optional: NotRequired[dict[
        str,
        (
            tuple[TypeString | list[TypeString]] |
            tuple[TypeString, NumberInputDict[int] | NumberInputDict[float] | StringInputDict]
        )
    ]]


class Node(ABC):
    FUNCTION = "execute"
    OUTPUT_NODE = False

    @property
    @abstractmethod
    def RETURN_TYPES(self) -> tuple[TypeString, ...]:
        pass

    @property
    @abstractmethod
    def CATEGORY(self) -> str:
        pass

    @classmethod
    @abstractmethod
    def INPUT_TYPES(cls) -> InputDict:
        pass

    @abstractmethod
    def execute(self) -> tuple[Any, ...] | None:
        pass
