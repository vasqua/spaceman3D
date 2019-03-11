import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Spaceman3D',
    version='0.0.1',
    author='Jeremy A. Seibert',
    author_email='Jaseibert2@eagles.usi.edu',
    description="Spaceman3D is a Package that parses satellite Two-Line Element (TLE) Data and creates 3D plots of the satellite's orbits.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jaseibert/Spaceman",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
