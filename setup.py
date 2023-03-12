import os
import setuptools
from pip._internal.req import parse_requirements

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

INSTALL_REQS = parse_requirements("requirements.txt", session="hack")

try:
    REQS = [str(ir.req) for ir in INSTALL_REQS]
except AttributeError:
    REQS = [str(ir.requirement) for ir in INSTALL_REQS]
    
setuptools.setup(
    name='pga_etl',
    version=os.environ["RELEASE_VERSION"],
    author="Sean Caldwell & Jamie Paton",
    author_email="sean.caldwell5@outlook.com",
    description="PGA tour api data collector (ETL)",
    include_package_data=False,
    zip_safe=False,
    install_requires=REQS,
    packages=setuptools.find_packages(exclude=
        [
            'src.flows',
            'src.flows.*',
            'src.setup',
            'src.setup.*',
            'src.tests',
            'src.tests.*',
            'setup.py'
        ]),
    setup_requires=[],
    py_modules=[],
    python_requires="==3.9"
)