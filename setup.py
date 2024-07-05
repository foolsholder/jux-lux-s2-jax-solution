from setuptools import find_packages, setup

with open('requirements.txt', 'r') as fin:
    reqs = fin.read().splitlines()

setup(
    name="jux",
    packages=find_packages(),
    include_package_data=True,
    version="0.1.0",
    install_requires=reqs,
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    test_suite="tests",
)