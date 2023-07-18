import subprocess
import sys

import setuptools  # type: ignore
from setuptools import Extension, setup

try:
    from numpy import __version__ as numpy_version
    from numpy import get_include
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])
    from numpy import __version__ as numpy_version
    from numpy import get_include

try:
    from Cython.Build import cythonize
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Cython"])
    from Cython.Build import cythonize  # type: ignore


ext_modules = cythonize([Extension("choldate._choldate", ["choldate/_choldate.pyx"], include_dirs=[get_include()])])

setup(
    name="choldate",
    version="0.1.0",
    packages=setuptools.find_packages(),
    include_package_data=True,
    ext_modules=ext_modules,
    install_requires=(base_packages := [f"numpy>={numpy_version}"]),
    zip_safe=False,
)
