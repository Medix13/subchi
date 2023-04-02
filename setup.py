from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name='subchi',
    version='1.1.0',
    description='A tool for checking subdomains of a domain',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Mahdi Pourgholami',
    url='https://github.com/Medix13/subchi',
    packages=find_packages(),
    install_requires=requirements,
    entry_points='''
        [console_scripts]
        subchi=subchi.subchi:main
    ''',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
