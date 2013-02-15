__author__ = 'jasonrudy'


from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy
from Cython.Build import cythonize


setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = cythonize([Extension("choldate", ["choldate.pyx"],include_dirs = [numpy.get_include()])
    ]), requires=['numpy']

)
