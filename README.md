# bitcoin-rpc
Bitcoin JSON RPC client in Python

AuthServiceProxy is an improved version of python-jsonrpc.

It includes the following generic improvements:

HTTP connections persist for the life of the AuthServiceProxy object
sends protocol 'version', per JSON-RPC 1.1
sends proper, incrementing 'id'
uses standard Python json lib
can optionally log all RPC calls and results
JSON-2.0 batch support
It also includes the following bitcoin-specific details:

sends Basic HTTP authentication headers
parses all JSON numbers that look like floats as Decimal, and serializes Decimal values to JSON-RPC connections.

### Installation
change the first line of setup.py to point to the directory of your installation of python 2.*
run setup.py
Note: This will only install bitcoinrpc. If you also want to install jsonrpc to preserve backwards compatibility, you have to replace 'bitcoinrpc' with 'jsonrpc' in setup.py and run it again.

Or simply install the library using pip:

pip install python-bitcoinrpc