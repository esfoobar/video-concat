# video-concat

This script searches for the videos in a folder you provide, creates a list of the videos in a text file and merges them.

## Installation

Check out this repository, `cd` into it and then install the Poetry dependencies with `poetry install`.

## Requirements

- Poetry
- FFMpeg

## File name requirements
- Files should have the following format: `{chapter}.{section}.{sub-section}_{Video_Title_Name}.mp4`
- If you have sub-sections, make sure all the parent sections have a `.0`, for example:
    - `4.0_Starting_with_Git`, `4.0.1_The_File_System` will put the `4.0.1` on top. To avoid that, rename the first file to `4.0.0_Starting_with_Git`

## Commands

To get a list of the commands, type: `poetry run python video_concat/video-concat.py`

### Create concat file list

To generate the list of files to be concatenated, do: `poetry run python video_concat/app.py create-concat-file -p "/path/to/file/files.txt"`

### Generate merged video file from file list

To generate the merged video from the files, do: `poetry run python video_concat/app.py create-merged-file -p "/path/to/file/files.txt" -o "/path/to/file/merged.mp4" -c "/path/to/chapters_file"`