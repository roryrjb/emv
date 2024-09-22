import subprocess
from setuptools import Command, setup, find_packages


class PyInstaller(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        subprocess.run(["pyinstaller", "--onefile", "--name", "emv", "cli.py"])


setup(
    name="emv",
    version="0.2",
    description="Rename files with your editor",
    url="https://github.com/roryrjb/emv",
    author="Rory Bradford",
    author_email="roryrjb@gmail.com",
    license="MIT",
    install_requires=[],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "emv=emv.emv:main",
        ],
    },
    zip_safe=False,
    cmdclass={
        "build_exe": PyInstaller,
    },
)
