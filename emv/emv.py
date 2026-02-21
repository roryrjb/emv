import os
import tempfile
import shlex
import subprocess
import sys


def main():
    files = sys.argv[1:]

    with tempfile.NamedTemporaryFile(
        mode="w+t", delete=False, encoding="utf-8"
    ) as tmpfile:
        filenames_file = tmpfile.name

        if files:
            src = files
        else:
            src = [f for f in os.listdir(".") if os.path.isfile(f)]
        tmpfile.write("\n".join(src))

    editor = os.environ.get(
        "EDITOR",
        "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin",
    )
    editor_cmd = shlex.split(editor, posix=True) + [filenames_file]
    subprocess.call(editor_cmd)

    with open(filenames_file, "r", encoding="utf-8") as tmpfile:
        dest = tmpfile.read().splitlines()

    os.remove(filenames_file)

    if len(src) != len(dest):
        print(
            "WARN: Number of files changed. Did you delete a line by accident? Aborting..",
            file=sys.stderr,
        )
        sys.exit(1)

    count = 0
    for s, d in zip(src, dest):
        if s != d:
            dd = os.path.dirname(d)

            if dd:
                os.makedirs(dd, exist_ok=True)
            os.rename(s, d)
            count += 1

    print(f"{count} files renamed.")
