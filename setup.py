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
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='sl',
    package_dir={'': 'src'},
    install_requires=['requests'],
    zip_safe=False
)