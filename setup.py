import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

top_dir, _ = os.path.split(os.path.abspath(__file__))

with open(os.path.join(top_dir, 'Version')) as f:
    version = f.readline().strip()

setuptools.setup(
    name="mlglass",
    version= version,
    author="Nikesh Bajaj",
    author_email="bajaj.nikey@gmail.com",
    description="MLglass: A Transparency with models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nikeshbajaj/mlglass",
    download_url = 'https://github.com/Nikeshbajaj/mlglass/tarball/' + version,
    packages=setuptools.find_packages(),
    license = 'MIT',
    keywords = 'Machine Learning, Visualizations, Weights, Decision Tree, Naive Bayes',
    classifiers=[
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Model Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',

        'Development Status :: 1 - Production/Stable',


    ],
    include_package_data=True,
    install_requires=['numpy','matplotlib','scipy','scikit-learn','python-picard']
)
