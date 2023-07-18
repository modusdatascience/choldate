# import numpy
# from Cython.Build import cythonize
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

# ext_modules = (
#     cythonize(
#         module_list=[
#             setuptools.Extension(
#                 "*",
#                 sources=["**/*.pyx"],
#                 include_dirs=[get_include()],
#             )
#         ],
#         compiler_directives={
#             "language_level": 3,
#             "binding": True,
#             "embedsignature": True,
#         },
#     ),
# )

setup(
    name="choldate",
    version="0.1.0",
    # packages=["choldate", "choldate.test"],
    packages=setuptools.find_packages(),
    include_package_data=True,
    # ext_modules=cythonize(extensions),
    ext_modules=ext_modules,
    # include_dirs=[numpy.get_include()],
    # install_requires=["numpy", "cython"],
    # install_requires=(base_packages := [f"numpy>={numpy_version}", "cython"]),
    install_requires=(base_packages := [f"numpy>={numpy_version}"]),
    zip_safe=False,
)
