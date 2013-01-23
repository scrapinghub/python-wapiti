import os
from distutils.core import setup, Extension


def _sources(srcdir):
    return [os.path.join(dirpath, fn)
            for dirpath, _, filenames in os.walk(srcdir)
            for fn in filenames if fn.endswith('.c')]

setup(
    name='wapiti',
    version='0.1',
    description="Python bindings for libwapiti",
    author="Adam Svanberg",
    author_email="asvanberg@gmail.com",
    py_modules=['wapiti'],
    ext_modules=[
        Extension(
            '_wapiti',
            include_dirs=['wapiti/src', 'libwapiti/src'],
            sources=_sources('wapiti/src') + _sources('libwapiti/src'),
            extra_compile_args=['-std=c99'],
            extra_link_args=['-lm', '-lpthread'],
        )
    ],
)
