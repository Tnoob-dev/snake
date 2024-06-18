import typer
from typing_extensions import Annotated
from pathlib import Path
from utils.io_utils import inputOutputCommands


app = typer.Typer()

@app.command("wf")
def create_file(file_name: Annotated[str, typer.Argument()]):

    string = input()
    inputOutputCommands(file_name, "w+", string)

@app.command("rf")
def read_file(file_name: Annotated[str, typer.Argument()]):

    content = inputOutputCommands(file_name, "r+")
    print(content)

@app.command("cf")
def copy_content(old_file: Annotated[str, typer.Argument()], new_file: Annotated[str, typer.Argument()]):
    
    content = inputOutputCommands(old_file, "r+")

    inputOutputCommands(new_file, "w+", content)

if __name__ == "__main__":
    app()