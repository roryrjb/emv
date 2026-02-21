from setuptools import setup, find_packages

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
)
