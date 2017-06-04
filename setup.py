#!/usr/bin/env python3

import glob
import os
import re

from setuptools import setup

init_path = os.path.join(os.path.dirname(__file__),
                         "radicale_infcloud", "__init__.py")
with open(init_path) as f:
    version = re.search(r'VERSION = "([^"]+)"', f.read()).group(1)
os.chdir("radicale_infcloud")
web_data = list(filter(os.path.isfile, glob.glob("web/**/*[!~]", recursive=True)))
os.chdir(os.pardir)

setup(
    name="Radicale_InfCloud",
    version=version,
    description="InfCloud for Radicale",
    author="Unrud",
    author_email="unrud@openaliasbox.org",
    url="http://github.com/Unrud/RadicaleWeb",
    license="GNU AGPL v3",
    platforms="Any",
    packages=["radicale_infcloud"],
    package_data={"radicale_infcloud": web_data})
