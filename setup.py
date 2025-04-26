from setuptools import setup, find_packages

setup(
    name="WaterQualityPrediction",
    version="1.0.0",
    author="Suvarchala Poluri",
    description="A machine learning project for predicting water potability.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Suvarchala-Poluri/Water-Quality-Prediction",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
        "pandas",
        "numpy",
        "scikit-learn",
        "matplotlib",
        "seaborn"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
