#!/usr/bin/env python3
import typer
import time
import os
from pathlib import Path
import datetime
import pytz

app = typer.Typer()


@app.command()
def create(
    filename: str = typer.Argument(..., help="Name of the file to create"),
    directory: str = typer.Option(
        None, "--dir", "-d", help="Directory to create the file in"
    ),
):
    """Create a file with a timestamp prefix (in seconds) using GMT-03:00 timezone."""
    # Get current timestamp using GMT-03:00 timezone
    gmt_minus_3 = pytz.timezone("America/Sao_Paulo")  # This timezone is GMT-03:00
    now = datetime.datetime.now(gmt_minus_3)

    # Timestamp in seconds (10 digits)
    current_timestamp = int(now.timestamp())

    # Create the new filename with timestamp prefix
    new_filename = f"{current_timestamp}_{filename}"

    # Use specified directory or current directory
    file_path = os.path.join(directory or os.getcwd(), new_filename)

    # Create an empty file with the new name
    Path(file_path).touch()

    typer.echo(f"Created file: {new_filename} (GMT-03:00)")
    typer.echo(f"Timestamp usado (seconds): {current_timestamp}")
    typer.echo(
        f"Para converter este timestamp: epochcli convert {current_timestamp}"
    )


@app.command()
def convert(
    epoch_time: int = typer.Argument(..., help="Unix timestamp to convert"),
    milliseconds: bool = typer.Option(
        False, "--ms", help="Treat the timestamp as milliseconds"
    ),
):
    """Convert a Unix timestamp to a human-readable date."""
    if milliseconds:
        # Convert from milliseconds to seconds
        timestamp = epoch_time / 1000
    else:
        timestamp = epoch_time

    # Convert timestamp to datetime
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    formatted_date = dt_object.strftime("%Y-%m-%d %H:%M:%S")

    typer.echo(f"Timestamp {epoch_time} corresponds to: {formatted_date}")
    typer.echo(
        f"UTC time: {datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')} UTC"
    )


if __name__ == "__main__":
    app()
