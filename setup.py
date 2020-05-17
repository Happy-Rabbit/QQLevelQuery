# coding: gb18030

from setuptools import setup

setup(
    name="qlquery",
    version="1.0",
    license="MIT",
    packages=['qlquery'],
    install_requires=[
        'my-fake-useragent',
        'requests',
        'beautifulsoup4'
    ],
    zip_safe=False
)