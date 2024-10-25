"""
Write a python function that can be executed by our model  
It will take in a note and save it to a file in data/notes.txt
"""

import os
from llama_index.core.tools import (
    FunctionTool,
)  # A tool that takes in a function that a model can use


# # Now wrap the function and kind of create an engine that the agent will be able to use


def save_note(note: str) -> str:
    """
    This tool saves a text-based note to a file for the user.
    """

    note_file = os.path.join("data", "notes.txt")

    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(note_file), exist_ok=True)

    try:
        with open(note_file, "a") as f:  # 'a' - append mode
            f.write(note + "\n")  # single note, add newline for readability
        return "Note saved successfully!"
    except Exception as e:
        return f"Error saving note: {e}"  # Provide more informative error message


note_engine = FunctionTool.from_defaults(
    fn=save_note,
    name="note_saver",
    description="This tool can save a text-based note to a file for the user.",
)
