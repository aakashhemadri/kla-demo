import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kla-demo",
    version="0.0.1",
    author="Aakash Hemadri",
    author_email="aakashhemadri123@gmail.com",
    description="kla-demo package",
    long_description="# A simple setup. - kla-demo",
    long_description_content_type="text/markdown",
    url="https://github.com/aakashhemadri/kla-demo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)