from setuptools import setup, find_packages

setup(
    name="mathsolver-pro",
    version="0.1.0",
    description="Advanced modular math library: algebra, statistics, calculus, geometry, financial engineering.",
    author="Samuel Zocchi",
    author_email="samuel.zocchi@gmail.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy>=1.21",
        "scipy>=1.7",
        "sympy>=1.8",
        "matplotlib>=3.4",
        "scikit-learn>=1.0"
    ],
    python_requires=">=3.8",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/samzoc/mathsolver_pro",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
