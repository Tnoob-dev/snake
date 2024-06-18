import typer
from pathlib import Path
from typing_extensions import Annotated
from typing import Optional


def inputOutputCommands(file_name: Annotated[str, typer.Argument()], method: str, content: Annotated[Optional[str], typer.Argument()] = None):

    with open(Path(file_name), method) as file:

        if method == "r" or method == "rb" or method == "r+":
            return file.read()
        elif method == "w" or method == "wb" or method == "w+":
            file.writelines(content)

