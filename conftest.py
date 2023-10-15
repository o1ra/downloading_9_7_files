import os
import shutil
import zipfile
import pytest

current_dir = os.path.dirname(os.path.abspath(__file__))
resources_files = os.path.join(current_dir, "resources")
file_dir = os.listdir(resources_files)
tmp = os.path.join(current_dir, "tmp")


@pytest.fixture(autouse=True)
def create_zipfile_with_file_from_resources():
    # create tmp
    if not os.path.isdir("tmp"):
        os.mkdir("tmp")
    # create zipfile
    os.chdir("resources")
    with zipfile.ZipFile("test.zip", mode="w") as zf:
        for file in file_dir:
            zf.write(file)
    shutil.move("test.zip", os.path.join(tmp, "test.zip"))
    os.chdir(current_dir)

    yield

    zf.close()

