from setuptools import setup, find_packages

setup(
    name='memoized',
    description="A simple memoization decorator that's also memory efficient on instance methods",
    long_description="",
    license='BSD-3',
    packages=find_packages('.'),
    install_requires=(),
    test_requires=(
        'nose==1.3.7',
    )
)