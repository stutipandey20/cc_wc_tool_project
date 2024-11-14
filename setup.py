

from setuptools import setup, find_packages

setup(
    name='ccwc_tool',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'argparse',
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'ccwc = wc_tool.ccwc:main',
        ],
    },
    description="Custom wc command-line tool",
    author="Stuti Pandey",
    author_email="stutip74@gmail.com",
    url="https://github.com/stutipandey20/wc_tool_project",
)
