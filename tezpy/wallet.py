class Wallet:
    ''' Wallet is a wrapper class around a keypair instance and a node '''
    def __init__(self, keypair, watchonly=False):
        self._watchonly = watchonly
        self._keypair = keypair

    @staticmethod
    def fromMnemonic(mnemonic):
        return Wallet(None)

    def update(self):
        ''' Trigger an update of the wallet informations, like balances, transactions and more ''' 
        pass

    def transfer(self, amount, destination):
        ''' Transfer and amount to a destination address '''
        if self._watchonly: raise ('Watch-only wallet')
        return False

    def getTransactions(self, flow='both', page=0, limit=25):
        ''' Return the list of received and sent transactions 
        
        Parameters:
            - flow: can be both (for in and out transactions), in or out
            - page: pagination page
            - limit: number of results        

        Returns a list of transactions
        '''
        return []

    def getBalance(self):
        ''' Return the balance of the wallet '''
        return 0.0