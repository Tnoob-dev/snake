"""
Main file from snake py
"""
from typing import List
import typer
from typing_extensions import Annotated
from utils.io_utils import inputOutputCommands

__version__ = "3.0.0"

app = typer.Typer()

@app.command("rf")
def read_file(file_name: Annotated[List[str], typer.Argument()]):
    """
    Read content from files
    """
    for file in file_name:
        content = inputOutputCommands(file, "r+")
        print(content)

@app.command("wf")
def create_file(file_name: Annotated[str, typer.Argument()]):
    """
    Write content in a file
    """
    data = []
    while True:
        string = input()
        if string.strip():
            data.append(string)
        else:
            break
    inputOutputCommands(file_name, "w+", '\n'.join(data))

@app.command("cf")
def copy_content(old_file: Annotated[str, typer.Argument()],
                 new_file: Annotated[str, typer.Argument()]):
    """
    Copy content from a old file to a new file
    """
    content = inputOutputCommands(old_file, "r+")
    inputOutputCommands(new_file, "w+", content)

@app.command("mixf")
def mix_content(files: Annotated[List[str], typer.Argument()],
                newfile: Annotated[str, typer.Argument()]):
    """
    Mix files into a new file
    """
    data = []
    for file in files:
        content = inputOutputCommands(file, "r+")
        data.append(content)
    inputOutputCommands(newfile, "w+", '\n'.join(data))

@app.command("end")
def endline_sign(file_name: Annotated[str, typer.Argument()]):
    """
    Mark the end of each line
    """
    content = inputOutputCommands(file_name, "r+")
    data = [i for i in content.split("\n")]
    for new_data in data:
        print(new_data + "$")

@app.command("lines")
def numbers_lines(file_name: Annotated[str, typer.Argument()]):
    """
    Count number of lines from a file
    """
    content = inputOutputCommands(file_name, "r+")

    data = [i for i in content.split("\n")]

    for i, new_data in enumerate(data):
        print(str(1+i) + " " + new_data)

if __name__ == "__main__":
    app()
