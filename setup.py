from setuptools import setup, find_packages

setup(
    name="holyrains_drops_automation",
    version="0.1.2",
    description="A package for airdrop automation.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author="Ercans",
    author_website="---",
    url="https://github.com/HolyRains/HolyRains-Drops-Automation",
    packages=find_packages(),
    install_requires=[
        "colorama",
        "requests",
        "brotli",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
