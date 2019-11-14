import logging
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException


class RPCBitcoinCoreCommand:
    def __init__(self, username, password, port):
        self.rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:%s"%(username, password, port), timeout=1000)

    def callCommand(self, command, hash):
        if(command is None or hash is None):
            raise Exception('The command or the hash is null')
        try:
            tx = self.rpc_connection.getrawtransaction(hash)
            logging.debug(tx)
            return "OK"
        except JSONRPCException as jsone:
            logging.warning('Exception generated: ' + str(jsone))
            return hash
