from setuptools import setup

setup(
    name='sl_api',
    version='1.0',
    description='Unoffical Python Interface to the SL API',
    long_description='Unoffical Python Interface to the SL API',
    url='https://github.com/IsakNyberg/SL_API',
    author='Isak Nyberg',
    author_email='isak@nyberg.dev',
    license='MIT',
    packages=['sl_api'],
    keywords='sl',
    scripts=["sl_api"],
    package_dir={'': 'src'},
    install_requires=['requests'],
    zip_safe=False
)