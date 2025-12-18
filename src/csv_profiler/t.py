import typer
import pathlib as Path
app = typer.Typer()



@app.command()
def profile(s: float):
    try:
        return float(s)
    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    
if __name__ == "__main__":
    app()