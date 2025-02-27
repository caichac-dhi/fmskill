import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("LICENSE") as fh:
    license = fh.read()

setuptools.setup(
    name="fmskill",
    version="0.6.dev1",
    install_requires=[
        "numpy",
        "pandas",
        "mikeio >= 0.7",
        "matplotlib",
        "xarray",
        "markdown",
        "jinja2",
        "requests",
    ],
    extras_require={
        "dev": [
            "pytest",
            "sphinx",
            "sphinx-book-theme",
            "black==20.8b1",
            "plotly >= 4.5",
        ],
        "test": [
            "pytest",
            "netCDF4",
            "openpyxl",
            "dask",
        ],
        "notebooks": [
            "nbformat",
            "nbconvert",
            "jupyter",
            "folium",
            "plotly",
            "geopandas",
        ],
    },
    entry_points="""
        [console_scripts]
            fmskill=fmskill.cli:report
    """,
    author="Jesper Sandvig Mariegaard",
    author_email="jem@dhigroup.com",
    description="Compare results from MIKE FM simulations with observations.",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DHI/fmskill",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
    ],
)
