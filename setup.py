import pathlib
import os
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent.resolve()

PACKAGE_NAME = "SampleName"
AUTHOR = "8loser"
AUTHOR_EMAIL = "8loser+pypi@gmail.com"
URL = "https://github.com/8loser/SampleName"
DOWNLOAD_URL = "https://pypi.org/project/SampleName"

print('----for test')
print(os.environ.get('GITHUB_github.ref'))
print(os.environ.get('github.ref'))

LICENSE = "MIT"
VERSION = "0.0.1"
VERSION = os.environ.get('GITHUB_SHA_SHORT')
DESCRIPTION = "產生隨機英文名稱或英文稱的中文翻譯"
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding="utf8")
LONG_DESC_TYPE = "text/markdown"

requirements = (HERE / "requirements.txt").read_text(encoding="utf8")
INSTALL_REQUIRES = [s.strip() for s in requirements.split("\n")]

CLASSIFIERS = [
    f"Programming Language :: Python :: 3.{str(v)}" for v in range(7, 12)
]
PYTHON_REQUIRES = ">=3.7"

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    license=LICENSE,
    author_email=AUTHOR_EMAIL,
    url=URL,
    download_url=DOWNLOAD_URL,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
    classifiers=CLASSIFIERS,
    include_package_data=True,
    package_data={
        'sampleName': ["*.json"],
    },
)
