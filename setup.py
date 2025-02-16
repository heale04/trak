#!/usr/bin/env python
from setuptools import setup

setup(
    name="traker_mod",
    version="0.3.2",
    description="TRAK: Attributing Model Behavior at Scale",
    long_description="Check https://trak.csail.mit.edu/ to learn more about TRAK",
    author="MadryLab",
    author_email="trak@mit.edu",
    license_files=("LICENSE.txt",),
    packages=["trak_mod"],
    install_requires=[
        "torch>=2.0.0",
        "numpy",
        "tqdm",
    ],
    extras_require={
        "tests": [
            "assertpy",
            "torchvision",
            "open_clip_torch",
            "wget",
            "scipy",
            "datasets",
            "transformers",
        ],
        "fast": ["fast_jl"],
    },
    include_package_data=True,
)
