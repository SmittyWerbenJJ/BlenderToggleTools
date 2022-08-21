import os
from pathlib import Path
import glob
import shutil
import tempfile
import webbrowser
from zipfile import ZipFile
import fileinput

current_filePath = Path(__file__)
workspace_root_dir = current_filePath.parent.parent
bin_dir = Path.joinpath(workspace_root_dir, "src/bin/")
serpens_dir = Path.joinpath(workspace_root_dir, "src/serpens/")
addon_updater_files_dir = workspace_root_dir / "src" / "python" / "AddonUpdater"
automation_template_dir = workspace_root_dir / "src/python/automation/template"
toggle_tools_release_dir = workspace_root_dir / "blender_toggle_tools"
toggle_tools_dir = workspace_root_dir / "src/python/toggleTools/"

# get latest serpens zip file
globs = glob.glob(str(serpens_dir / "*"))
latest_serpens_zip = Path(max(globs, key=os.path.getctime))

# extract zip in temp folder -> work in this folder
print("Creating temp dir ...")
with tempfile.TemporaryDirectory() as tmpdirname:
    tmpdir = Path(tmpdirname)

    print("extracting ", latest_serpens_zip.name, "...")
    with open(latest_serpens_zip, "rb") as f:
        zfile = ZipFile(f)
        for f in zfile.namelist():
            zfile.extract(f, str(tmpdir))
    temp_addon_dir = tmpdir / Path(os.listdir(tmpdir)[0])

    # fetch init.py
    print("fetching init file ...")
    initFile: Path = None
    for root, dir, files in os.walk(temp_addon_dir):
        for f in files:
            if "__init__.py" in f:
                initFile = Path(os.path.join(root, f))
            break

    # cut bl_info from init.py
    print("extracting bl_info ...")
    blinfo: list[str] = []
    oldcontents = open(initFile).readlines()
    with open(initFile, mode="wt") as f:
        skip = False
        for line in oldcontents:
            if "bl_info = {" in line:
                skip = True

            if skip:
                blinfo.append(line)
            else:
                f.write(line)

            if skip and "}" in line:
                skip = False

    # overwrite __init__.py file from template
    print("overwriting init file ...")
    template_license = automation_template_dir / "license"
    template_initPy = automation_template_dir / "__init__.py"
    template_blInfo = blinfo

    with open(initFile, "w") as f:
        for line in open(template_license).readlines():
            f.write(line)
        f.write(os.linesep)
        for line in template_blInfo:
            f.write(line)
        f.write(os.linesep)
        for line in open(template_initPy).readlines():
            f.write(line)
        f.write(os.linesep)

    # copy addon updater next to init.py
    print("copying addon updater files ...")
    for root, _, files in os.walk(addon_updater_files_dir):
        for file in files:
            src = os.path.join(root, file)
            dst = str(initFile.parent)
            try:
                shutil.copy(src, dst)
            except Exception:
                pass

    # copy toggle tools next to init.py
    for f in toggle_tools_dir.iterdir():
        shutil.copy(f, initFile.parent)

    # zip temp dir
    print("zippiing up ...")

    zipfile = shutil.make_archive(
        base_name="CPU" + latest_serpens_zip.stem,
        format="zip",
        root_dir=tmpdirname,
        base_dir=os.listdir(tmpdirname)[0],
    )

    # move zip file to bin dir
    print("moving zip ...")
    zipfile = shutil.move(zipfile, str(bin_dir / Path(zipfile).name))

    # extract zip file to blender_toogle_tools
    print("clearing extract dir ...")
    for root, dirs, files in os.walk(toggle_tools_release_dir):
        for d in dirs:
            shutil.rmtree(os.path.join(root, d), ignore_errors=True)
        for f in files:
            shutil.rmtree(os.path.join(root, f), ignore_errors=True)

    print("final unzipping ...")
    shutil.unpack_archive(zipfile, workspace_root_dir)
