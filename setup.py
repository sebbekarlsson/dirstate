from setuptools import setup, find_packages


setup(
    name='dirstate',
    version='1.0.2',
    install_requires=[],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dirstate = dirstate.bin:run'
        ]
    }
)
