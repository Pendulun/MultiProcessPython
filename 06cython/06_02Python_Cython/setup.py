#Definimos os módulos cython a serem compilados
#Para compilar, use o seguinte comando:
#python .\setup.py build_ext --inplace
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(['computa.pyx'])
)