from setuptools import setup, find_packages

setup(
    name="my_id",
    version="1.0.0",
    url="https://github.com/Sam-Strand/my_id",
    author="Садовский М.К.",
    author_email="i@maxim-sadovskiy.ru",
    packages=find_packages(),
    install_requires=[
        "pydantic>=2.5.0",
    ],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
    ],
)