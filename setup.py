import setuptools

setuptools.setup(
    name="tinarm",
    version="0.1",
    author="Martin West, Chris Wallis",
    description="TINARM - Node creation tool for TAE workers",
    url="https://github.com/TinArmEngineering/tinarm",
    author_email="chris@tinarmengineering.com",
    license="MIT",
    packages=["tinarm"],
    install_requires=[
        "pika",
        "python_logging_rabbitmq",
        "requests",
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
    ],
)
