import typer, string
from typing import List
from typing_extensions import Annotated
from utils.io_utils import inputOutputCommands

__version__ = "2.0.0"

app = typer.Typer()

@app.command("rf")
def read_file(file_name: Annotated[List[str], typer.Argument()]):
    
    for file in file_name:
        content = inputOutputCommands(file, "r+")
        print(content)

@app.command("wf")
def create_file(file_name: Annotated[str, typer.Argument()]):
    data = []
    while True:
        string = input()
        if string.strip():
            data.append(string)
        else:
            break
    inputOutputCommands(file_name, "w+", '\n'.join(data))

@app.command("cf")
def copy_content(old_file: Annotated[str, typer.Argument()], new_file: Annotated[str, typer.Argument()]):
    
    content = inputOutputCommands(old_file, "r+")
    inputOutputCommands(new_file, "w+", content)

@app.command("mixf")
def mix_content(files: Annotated[List[str], typer.Argument()], newfile: Annotated[str, typer.Argument()]):

    data = []
    for file in files:
        content = inputOutputCommands(file, "r+")
        data.append(content)
    
    inputOutputCommands(newfile, "w+", '\n'.join(data))

@app.command("v")
def unprintable_values(file_name: Annotated[str, typer.Argument()]):
    
    content = inputOutputCommands(file_name, "r+")

    for caracter in content:
        if caracter not in string.printable:
            print(f"El caracter {caracter} no es imprimible")

if __name__ == "__main__":
    app()