import setuptools

REQUIRED = [
    "numpy",
    "pandas"
]

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='stevedata-smsinclair',
    version='0.0.1',
    author='SMSinclair@gmail.com',
    author_email='smsinclair@gmail.com',
    description='Some very basic DataFrame tools.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=
    'https://github.com/SMSinclair/stevedata',
    packages=setuptools.find_packages(),
    classifiers=['Programming Language :: Python :: 3',
                 'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
                 'Operating System :: OS Independent'],
)

