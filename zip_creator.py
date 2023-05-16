import zipfile
import pathlib


def make_archive(filepaths, destination_dir):
    new_destination_path = pathlib.Path(destination_dir, "compressed.zip")
    with zipfile.ZipFile(new_destination_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


