from distutils.core import setup, Extension

setup(name="libthai", version="0.0.1",
      ext_modules=[ 
        Extension("libthai", 
                  ["libthai.c"],
                  libraries=['thai'])])

