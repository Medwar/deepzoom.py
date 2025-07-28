#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="DeepZoomToolsMindat",
    version="2.0.1",
    author="Pavel.Martynov",
    author_email="pavel.bw@gmail.com",
    description="Python tools for generating Deep Zoom images (DZI) and \
collections (DZC) for the use with Silverlight Deep Zoom, Seadragon Ajax, \
Seadragon Mobile, and OpenZoom. Fork - added Pillow 11 compartibility, webp tile format",
    keywords="deepzoom seadragon dzi dzc seadragonajax seadragonmobile silverlightdeepzoom microsoft openzoom",
    packages=find_packages(),
    license="BSD 3-Clause License",
    install_requires=["Pillow>=11"],
    url="https://github.com/Mindat-org/deepzoom.py",
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Utilities",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
    ],
)
