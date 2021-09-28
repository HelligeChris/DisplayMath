from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='DisplayMath',
    url='https://github.com/HelligeChris/DisplayMath',
    author='HelligeChris',
    # Needed to actually package something
    packages=['DisplayMath'],
    # Needed for dependencies
    install_requires=['sympy', 'IPython'],
    # *strongly* suggested for sharing
    version='0.0.2',
    # The license can be anything you like
    license='MIT',
    description='Display latex in python',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read(),
)