from setuptools import setup, find_packages

setup(
    name="py_first_ever_lib",
    version="0.0.1",
    author="Iana M",
    author_email="user.useriana@gmail.com",
    url="",
    description="Takes an image and anlyses it",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    entry_points={"console_scripts": ["py_first_ever_lib = py_first_ever_lib.main:main"]},
)