from .nodes import Int, Float, String, StringMultiline


NODE_CLASS_MAPPINGS = {
    "int": Int,
    "float": Float,
    "string": String,
    "string_multiline": StringMultiline
}


NODE_DISPLAY_NAME_MAPPINGS = {
    "int": "int",
    "float": "float",
    "string": "string",
    "string_multiline": "string (multiline)"
}
