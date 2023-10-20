from typing import TypeVar
from .base import Node, InputDict


T = TypeVar("T")

ABS_MAX = 1125899906842624


class CategoryTyped:
    CATEGORY = "utils/Primitive Types"


class PassthroughExecute:
    FUNCTION = "execute"

    def execute(self, **kwargs: T) -> tuple[T, ...] | None:
        if kwargs:
            return tuple(kwargs.values())
        return None


class Int(PassthroughExecute, CategoryTyped, Node):
    @classmethod
    def INPUT_TYPES(cls) -> InputDict:
        return dict(
            required=dict(
                value=("INT", dict(default=0, min=-ABS_MAX, max=ABS_MAX, step=1, display="number"))
            )
        )

    RETURN_TYPES = ("INT",)


class Float(PassthroughExecute, CategoryTyped, Node):
    @classmethod
    def INPUT_TYPES(cls) -> InputDict:
        return dict(
            required=dict(
                value=("FLOAT", dict(default=0, min=-ABS_MAX, max=ABS_MAX, step=1, display="number"))
            )
        )

    RETURN_TYPES = ("FLOAT",)


class String(PassthroughExecute, CategoryTyped, Node):
    @classmethod
    def INPUT_TYPES(cls) -> InputDict:
        return dict(
            required=dict(
                text=("STRING", dict(default="", multiline=False))
            )
        )

    RETURN_TYPES = ("STRING",)


class StringMultiline(PassthroughExecute, CategoryTyped, Node):
    @classmethod
    def INPUT_TYPES(cls) -> InputDict:
        return dict(
            required=dict(
                text=("STRING", dict(default="", multiline=True))
            )
        )

    RETURN_TYPES = ("STRING",)
