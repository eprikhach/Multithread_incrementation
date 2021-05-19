from distutils.core import setup, Extension

incr_module = Extension('incr', sources=['main.cpp'],
                        extra_compile_args=["-fPIC", "-std=c++11"],
                        language='c++')
setup(name='incr_extension', version='1.0',
      description='This is a incrementation package', ext_modules=[incr_module])
