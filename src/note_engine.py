from llama_index.tools import FunctionTool
import os

note_file = os.path.join(os.path.dirname(__file__), "data", "note.txt")

def save_note(note: str):
    if not os.path.exists(note_file):
        with open(note_file, "w") as f:
        
    with open(note_file, "a") as f:
        f.writelines([note + "\n"])
    return "note saved"


note_engine = FunctionTool(
    fn=save_note,
    name="note_saver",
    description="Save a note to a file",
)