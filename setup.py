""" stevedata - a collection of Data Science helper functions
"""

import setuptools

REQUIRED = [
    "numpy",
    "pandas"
]

with open('README.md', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='stevedata-smsinclair',
    version='0.0.1',
    author='SMSinclair',
    author_email='smsinclair@gmail.com',
    description='Basic DataFrame tools. Split dates or report nulls.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/SMSinclair/stevedata',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=REQUIRED,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'   
        'Operating System :: OS Independent'
    ],
)

