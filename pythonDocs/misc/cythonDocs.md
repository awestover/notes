
#helloWorld.pyx
def hi():
  print("Hello World")

#setup.py
from distutils.core import setup
from Cython.Build import cythonize
setup(ext_modules = cythonize("helloworld.pyx"))

#terminal
python setup.py build_ext --inplace

#runner.py
from helloWorld import hi
hi()

