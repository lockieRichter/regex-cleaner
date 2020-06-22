import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="regex_cleaner",  # Replace with your own username
    version="0.0.1",
    author="Lockie Richter",
    author_email="richter.lockie@gmail.com",
    description="A small package to remove comments from verbose regex patterns.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lockieRichter/regex_cleaner",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
