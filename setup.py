from setuptools import setup, find_packages

setup(
    name='Software Engineering Project',
    version='1.0.0',
    packages=find_packages(),
    description='Flood detection model',
    tests_require=['pytest'],
    author='Nelluru, Dedeepya',
    author_email='dnellur@ncsu.edu',
    url='https://github.com/dnellur4/flood_detection_model',
    python_requires='>=3.7',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Topic :: Project",
    ],
    license='MIT'
)
