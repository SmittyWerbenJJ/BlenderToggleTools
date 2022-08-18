from ast import keyword
from inspect import currentframe
import os
from pathlib import Path
import tempfile

from zipfile import ZipFile
import shutil
import webbrowser

current_filePath = Path(__file__).resolve()
workspace_root_dir = current_filePath.parent.parent.resolve()
serpens_bin_dir = Path.joinpath(workspace_root_dir, "bin/serpens/").resolve()
release_dir = Path.joinpath(workspace_root_dir, "bin/release/").resolve()
serpens_zip_path = Path.joinpath(serpens_bin_dir, os.listdir(serpens_bin_dir)[-1])
auto_update_src_files_dir_path = Path.joinpath(
    workspace_root_dir, "src/blender-addon-updater"
)

init_file_path: Path = None
tab = "    "


class contentReplacer:
    keyword: str
    replacement: list[str]
    replacementOneLine: str

    def __init__(self, kwd, replacements=[], replacementOneLine="") -> None:
        self.keyword = kwd
        self.replacement = replacements
        self.replacementOneLine = replacementOneLine


def createTempDir():
    """create temp dirs"""
    print("Creating temp dirs ...")
    tmpdir = Path(tempfile.mkdtemp())
    # tmpdir_extract = Path(tempfile.mkdtemp())
    # os.makedirs(tmpdir_extract, exist_ok=True)
    # os.makedirs(tmpdir_toggleTools, exist_ok=True)
    webbrowser.open(release_dir)
    return tmpdir


def extractSerpensPackedZip(serpens_zip_path: Path, dstPath: Path):
    """extracting serpens-zip files to temp dir"""
    print("extracting ", serpens_zip_path.name, "...")
    with open(serpens_zip_path, "rb") as f:
        zfile = ZipFile(f)
        for f in zfile.namelist():
            zfile.extract(f, str(dstPath))
    for root, dir, _ in os.walk(dstPath):
        return Path(os.path.join(root, dir[0]))


def getIniPyFile(serpensExtractZipPath: Path):
    print("finding __init__.py file in extracted Files ...")
    for root, _, files in os.walk(serpensExtractZipPath):
        for f in files:
            if "__init__.py" in f:
                print("init file found...")
                return Path(os.path.join(root, f))
    print("NO init file found")
    return None


def indexof(_str: str, _sub: str):
    """_str: the string to search through
    _sub: the substring to find
    returns: -1 no substring or the start index of the substring"""
    try:
        index = str.index(_str, _sub)
    except ValueError:
        index = -1
    return index


def replaceContentsInFile(file_path: Path, *replacerContents: contentReplacer):
    print("writing new content to", file_path.name, "...")
    newcontents = []
    contents = []

    # reading init file into var
    with open(str(file_path), "r") as f:
        contents = f.readlines()

    # replacing lines with its respective replacercontent
    for idx, line in enumerate(contents):
        noReplace = True
        for replContent in replacerContents:
            index = indexof(line, replContent.keyword)
            if index != -1:
                noReplace = False
                replacedContent = line[:index] + replContent.replacementOneLine
                newcontents.append(replacedContent)
        if noReplace == True:
            newcontents.append(line)
    # writing to file
    with open(str(file_path), "w") as f:
        for line in newcontents:
            f.write(line)


def writeContentsToFile(file_path: Path, *replacerContents: contentReplacer):
    newcontents = []
    contents = []
    print("writing new content to", file_path.name, "...")

    # reading init file into var
    with open(str(file_path), "r") as f:
        contents = f.readlines()

    # adding auto update code to init file
    for idx, line in enumerate(contents):
        newcontents.append(line)
        for c in replacerContents:
            if c.keyword in line:
                for x in c.replacement:
                    newcontents.append(x + "\n")

    # writing init file
    with open(str(file_path), "w") as f:
        for line in newcontents:
            f.write(line)


def copyAutoUpdaterFilesIntoExtractedZipDir(extractedZipdir):
    """returns the filepath of addon_updater_ops"""
    # copy auto updater files into zip dir
    print("copying auto update files to extracted Files...")
    for root, _, f in os.walk(str(auto_update_src_files_dir_path)):
        if "addon_updater.py" in f:
            shutil.copy2(os.path.join(root, "addon_updater.py"), extractedZipdir)
            addonUpdaterPyFilePath = extractedZipdir.joinpath("addon_updater.py")
        if "addon_updater_ops.py" in f:
            shutil.copy2(os.path.join(root, "addon_updater_ops.py"), extractedZipdir)
            addonUpdaterOpsPyFilePath = extractedZipdir.joinpath("addon_updater_ops.py")
    return addonUpdaterOpsPyFilePath


def copyUpdaterUIToZipDir(addon_temp_Path):
    print("copying updater UI to extracted Files...")
    shutil.copy2(
        workspace_root_dir.joinpath("src/addon_updater_ui.py"), addon_temp_Path
    )


def makeZipFile(zipRoot, name):
    print("creating zip File ... ")
    webbrowser.open(Path(zipRoot))

    archive = shutil.make_archive(
        base_name=name, format="zip", root_dir=zipRoot, base_dir=os.listdir(zipRoot)[0]
    )
    return archive


def editingIniPyFile():
    """editing '__ini__.py' file ..."""
    print("editing '__ini__.py' file ...")

    import_contents = contentReplacer(
        "import ", ["from . import addon_updater_ops", "from . import addon_updater_ui"]
    )

    register_content = contentReplacer(
        "def register():",
        [
            tab + "addon_updater_ops.register(bl_info)",
            tab + "addon_updater_ui.register()",
        ],
    )  # searchtags: [replacing lines]

    unregister_content = contentReplacer(
        "def unregister():",
        [
            tab + "addon_updater_ops.unregister()",
            tab + "addon_updater_ui.unregister()",
        ],
    )  # searchtags: [replacing lines]
    replace_addonUpdater = contentReplacer(
        'updater.addon = "addon_updater_demo"',
        replacementOneLine='updater.addon = "blender_toggle_tools"',
    )
    replace_minVersion = contentReplacer(
        "updater.version_min_update = (0, 0, 0)",
        replacementOneLine="updater.version_min_update = (0, 1, 0)",
    )
    replace_useReleases = contentReplacer(
        "updater.use_releases", replacementOneLine="updater.use_releases = True"
    )
    replace_website = contentReplacer(
        "updater.website =",
        replacementOneLine='updater.website = "https://github.com/SmittyWerbenJJ/BlenderToggleTools"',
    )
    replace_Repo = contentReplacer(
        "updater.repo = ", replacementOneLine='updater.repo = "BlenderToggleTools"'
    )
    replace_User = contentReplacer(
        "updater.user = ", replacementOneLine='updater.user = "SmittyWerbenJJ"'
    )
    # create temp dir

    tmpDir = createTempDir()

    # extract serpens zip to temp dir
    addon_temp_Path = extractSerpensPackedZip(serpens_zip_path, tmpDir)
    addonUpdaterOpsPyFilePath = copyAutoUpdaterFilesIntoExtractedZipDir(addon_temp_Path)
    copyUpdaterUIToZipDir(addon_temp_Path)

    # find init file in extracted Files
    init_file_path = getIniPyFile(tmpDir)

    # setting auto update settings in init file
    writeContentsToFile(
        init_file_path, import_contents, register_content, unregister_content
    )

    # setting auto update settings in addon_updater_ops file

    replaceContentsInFile(
        addonUpdaterOpsPyFilePath,
        replace_addonUpdater,
        replace_minVersion,
        replace_useReleases,
        replace_website,
        replace_Repo,
        replace_User,
    )

    zipfile = makeZipFile(
        tmpDir,
        tmpDir.joinpath(serpens_zip_path.stem),
    )

    print("moving zip to release dir ...")
    shutil.move(zipfile, release_dir)

    print("DONE!")


def run():
    editingIniPyFile()


run()
