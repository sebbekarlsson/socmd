from setuptools import setup, find_packages


setup(
    name='socmd',
    version='1.0',
    install_requires=[
        ''
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'socmd-client = socmd.client:run',
            'socmd-server = socmd.server:run'
        ]
    }
)
