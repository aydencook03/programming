from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize('n_body_physics.pyx')
)
