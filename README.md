# video-concat

This script searches for the videos in a folder you provide, creates a list of the videos in a text file and merges them.

## Requirements

- Poetry
- FFMpeg

## Installation

Check out this repository, `cd` into it and then install the Poetry dependencies with `poetry install`.

## Commands

To get a list of the commands, type: `poetry run python video_concat/video-concat.py`

### Create concat file list

To generate the list of files to be concatenated, do: `poetry run python video_concat/app.py create-concat-file -p "/path/to/file/files.txt"`

### Generate merged video file from file list

To generate the merged video from the files, do: `poetry run python video_concat/app.py create-merged-file -p "/path/to/file/files.txt" -o "/path/to/file/merged.mp4"`