from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="epub-metadata",
    version="1.0.0b0",
    author="ThanatosDi",
    author_email="ThanatosDi@kttsite.com",
    description="https://github.com/ThanatosDi/epub-metadata",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThanatosDi/epub-metadata",
    packages=find_packages(),
    install_requires=[
        'arrow',
    ],
    entry_points={
        'console_scripts': [

        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Win32 (MS Windows)",
        "Topic :: Documentation :: Sphinx",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries",
        ""
    ],
)
