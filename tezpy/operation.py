class Operation:
    def __init__(self, kind):
        self.kind = kind

    def sign(self, key):
        pass

    def toJson(self):
        return {
            'kind': self.kind
        }


class ActivateOperation(Operation):
    KIND = 'activate_account'

    def __init__(self, pkh, secret):
        super().__init__(self.KIND)
        self.pkh = pkh
        self.secret = secret

    def toJson(self):
        j = super.toJson()
        j['pkh'] = self.pkh
        j['secret'] = self.secret
        return j

    @staticmethod
    def fromJson(j):
        return ActivateOperation(j['pkh'], j['secret'])


class BallotOperation(Operation):
    KIND = 'ballot'

    def __init__(self):
        raise('not implemented yet')

    def toJson(self):
        return super.toJson()

    @staticmethod
    def fromJson(j):
        return BallotOperation()


class ManagerOperation(Operation):
    def __init__(self, kind, fee, gas_limit, storage_limit):
        super().__init__(kind)
        self.fee = fee
        self.gas_limit = gas_limit
        self.storage_limit = storage_limit

    def toJson(self):
        j = super.toJson()
        j['fee'] = self.fee
        j['gas_limit'] = self.gas_limit
        j['storage_limit'] = self.storage_limit
        return j


class TransactionOperation(ManagerOperation):
    KIND = 'transaction'

    def __init__(self, destination, amount, fee, gas_limit=None, storage_limit=None):
        if storage_limit == None:
            storage_limit = 0
        if gas_limit == None:
            gas_limit = 200
        super().__init__(self.KIND, fee, gas_limit, storage_limit)
        self.destination = destination
        self.amount = amount

    def toJson(self):
        j = super.toJson()
        j['destination'] = self.destination
        j['amount'] = self.amount
        return j

    @staticmethod
    def fromJson(j):
        return TransactionOperation(j['destination'], j['amount'], j['fee'], j['gas_limit'], j['storage_limit'])


class OriginationOperation(ManagerOperation):
    KIND = 'originate'

    def __init__(self):
        raise('not implemented yet')

    def toJson(self):
        return super.toJson()

    @staticmethod
    def fromJson(j):
        return OriginationOperation()


class RevealOperation(ManagerOperation):
    KIND = 'reveal'

    def __init__(self):
        raise('not implemented yet')

    def toJson(self):
        return super.toJson()

    @staticmethod
    def fromJson(j):
        return RevealOperation()


class DelegationOperation(ManagerOperation):
    KIND = 'delegation'

    def __init__(self, delegate, fee, gas_limit=None, storage_limit=None):
        if storage_limit == None:
            storage_limit = 0
        if gas_limit == None:
            gas_limit = 0
        super().__init__(self.KIND, fee, gas_limit, storage_limit)
        self.delegate = delegate

    def toJson(self):
        j = super.toJson()
        j['delegate'] = self.delegate
        return j

    @staticmethod
    def fromJson(j):
        return DelegationOperation(j['delegate'], j['fee'], j['gas_limit'], j['storage_limit'])


OPERATION_TYPES = [
    ActivateOperation,
    BallotOperation,
    TransactionOperation,
    OriginationOperation,
    RevealOperation,
    DelegationOperation
]


def fromJson(j):
    ''' Deserialize a json operation '''
    for x in OPERATION_TYPES:
        if x.KIND == j['kind']:
            return x.fromJson(j)
    return None
