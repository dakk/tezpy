class Operation:
    def __init__(self):
        pass

    def sign(self, key):
        pass


class ActivateOperation(Operation):
    def __init__(self, kyccode):
        pass


class BallotOperation(Operation):
    def __init__(self, period, proposal, ballot):
        pass


class ManagerOperation(Operation):
    def __init__(self):
        pass


class TransactionOperation(ManagerOperation):
    def __init__(self, destination, value):
        pass

    def serialize(self):
        return b''


class OriginationOperation(ManagerOperation):
    def __init__(self):
        pass


class RevealOperation(ManagerOperation):
    def __init__(self):
        pass


class DelegationOperation(ManagerOperation):
    def __init__(self):
        pass


def deserialize(raw):
    ''' Deserialize a raw hex operation '''
    return None