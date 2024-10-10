import os, sys
from setuptools import setup, Extension, find_packages

try:
    from Cython.Build import cythonize
    import numpy
    extensions = cythonize([
        Extension("idr.inv_cdf", 
                  ["idr/inv_cdf.pyx", ],
                  include_dirs=[numpy.get_include()], compiler_directives={'language_level' : "3"}),
    ])
except ImportError:
    import numpy
    extensions = [
        Extension("idr.inv_cdf", 
                  ["idr/inv_cdf.c", ],
                  include_dirs=[numpy.get_include()]),
    ]

def main():
    if sys.version_info.major <= 2:
        raise ValueError( "IDR requires Python version 3 or higher" )
    setup(
        name = "idr",
        version = "2.0.5",

        author = "Nathan Boley",
        author_email = "npboley@gmail.com",

        ext_modules = extensions,     
        
        python_requires = ">=3.7",

        install_requires = [ 'scipy>=0.13.0', 'numpy'  ],

        extras_require={'PLOT': 'matplotlib'},

        packages= ['idr',],

        scripts =  ['./bin/idr',],

        description = ("IDR is a method for measuring the reproducibility of " + 
                       "replicated ChIP-seq type experiments and providing a " +
                       "stable measure of the reproducibility of identified " +
                       "peaks."),

        license = "GPL3",
        keywords = "IDR",
        url = "https://github.com/nboley/idr",

        
        classifiers=[
            "Programming Language :: Python :: 3",
            "Development Status :: 5 - Production/Stable",
            "Topic :: Scientific/Engineering :: Bio-Informatics",
            "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        ],
    )

if __name__ == '__main__':
    main()
