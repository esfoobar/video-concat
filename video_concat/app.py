import subprocess
import sys
import click
from pathlib import Path
import os
from datetime import timedelta

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
def create_video_list(file_list_path: str, sort_alpha: bool):
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
    help="Generate concatenated video file and the timestamp list for YouTube",
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
    # cmd = f'ffmpeg -f concat -safe 0 -i "{file_list_path}" -c copy "{output_video_file}"'
    # subprocess.call(cmd, shell=True)

    # read the files list
    file_list_path = Path(file_list_path)
    with open(file_list_path) as f:
        files = []
        for line in f:
            slashes = line.split("/")
            file_name = slashes[len(slashes) - 1][:-2]
            file_path = line.split("'")[1]

            # get the video duration info
            result = subprocess.run(
                [
                    "ffprobe",
                    "-v",
                    "error",
                    "-show_entries",
                    "format=duration",
                    "-of",
                    "default=noprint_wrappers=1:nokey=1",
                    "-sexagesimal",
                    file_path,
                ],
                stdout=subprocess.PIPE,
            )
            result_str = result.stdout.decode("utf-8")
            period = result_str.index("\n")
            duration = result_str[:period]

            files.append({"file_name": file_name, "duration": duration})

    # calculate total length
    running_length = timedelta()

    def parse_ts(ts: str) -> timedelta:
        h, m, s = ts.split(":")
        return timedelta(hours=int(h), minutes=int(m), seconds=float(s))

    i = 0
    for file in files:
        breakpoint()
        running_length += parse_ts(file["duration"])
        running_length_string = str(running_length)
        point = running_length_string.index(".")
        files[i]["running_length"] = running_length_string[:point]
        i += 1

    print(files)


if __name__ == "__main__":
    cli()
