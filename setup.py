
#!/usr/bin/env python

from distutils.core import setup

setup(
    name='pybitcoinrpc',
    version='1.0',
    description='Enhanced version of python-jsonrpc for use with Bitcoin',
    long_description=open('README.md').read(),
    author='Omidiora Samuel',
    author_email='<samparsky@gmail.com>',
    maintainer='Omidiora Samuel',
    maintainer_email='<samparsky@gmail.com>',
    url='https://github.com/blockchain-etl/bitcoin-rpc',
    packages=['bitcoinrpc'],
    classifiers=[
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)', 'Operating System :: OS Independent'
    ]
)