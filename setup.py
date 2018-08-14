from setuptools import setup, find_packages

setup(name='pypuma',
    version='0.2',
    description='Python implementation of PUMA, LIONESS.',
    url='https://github.com/aless80/PyPuma',
    author='Alessandro Marin',
    author_email='AlessandroMarin80@gmail.com',
    license='MIT',
    packages=['pypuma'],
    install_requires=['pandas',
    'numpy',
    'networkx',
    'matplotlib',
    'scipy'
    ],
    zip_safe=False)
