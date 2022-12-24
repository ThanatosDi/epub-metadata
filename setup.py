from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="epub-metadata",
    version="1.0.2b0",
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
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Win32 (MS Windows)",
        "Framework :: Pytest",
        "Topic :: Documentation :: Sphinx",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries",
        ""
    ],
)
