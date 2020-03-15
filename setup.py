from setuptools import setup,find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='machine-lib-rpigpio',
    version='0.1.0',
    author='featherfly',
    author_email='featherfly@foxmail.com',
    description="macropython machine lib implementation with RPi.GPIO for raspberrypi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/featherfly/machine-lib-gpio",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)