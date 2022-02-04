from email.policy import default
from subprocess import call
import sys
from xmlrpc.client import Boolean
import click
from pathlib import Path
import os
from subprocess import call

from utils import get_module_logger

logger = get_module_logger(__name__)


@click.group()
def cli():
    """Video file concatenation script using ffmpeg"""

    pass


@cli.command(
    help="Create a text file with the videos",
)
@click.option(
    "-p",
    "--file-list-path",
    help="Path to the directory where the videos are locates.",
)
@click.option(
    "-s",
    "--sort-alpha",
    is_flag=True,
    default=True,
    help="Sort the files alphabetically.",
)
def create_video_list(file_list_path: str, sort_alpha: Boolean):
    """CLI command to create a text file with the videos in that folder"""

    logger.info("Reading files from Path")

    file_list = []
    for file in os.listdir(file_list_path):
        if file.endswith("mp4"):
            file_list.append(file)

    if sort_alpha:
        logger.info("Sorting files alphabetically")
        file_list.sort()

    logger.info("Writing file list")

    # open the file
    file_list_path = Path(file_list_path)
    f = open(file_list_path / "files.txt", "wb")

    contents = ""

    for file in file_list:
        contents += "file '" + str(file_list_path / file) + "'\n"

    f.write(contents.encode())
    f.close()

    logger.info(f"File generated: {file_list_path / 'files.txt'}")

    sys.exit()


@cli.command(
    help="Generate concatenated video file",
)
@click.option(
    "-p",
    "--file-list-path",
    help="Path to the file list.",
)
@click.option(
    "-o",
    "--output-video-file",
    help="Path to the output file.",
)
def create_merged_file(file_list_path: str, output_video_file: str):

    logger.info("Generating concatenated file")
    cmd = f'ffmpeg -f concat -safe 0 -i "{file_list_path}" -c copy "{output_video_file}"'
    call(cmd, shell=True)


if __name__ == "__main__":
    cli()
