from ast import arg


def F(X, Y, Z):
    return (X & Y) | (~X & Z)


def G(X, Y, Z):
    return (X & Z) | (Y & ~Z)


def H(X, Y, Z):
    return X ^ Y ^ Z


def I(X, Y, Z):
    return Y ^ (X | ~Z)


class MD5:

    def __init__(self):
        # Initialize buffers, etc.
        self.length: int=0
        self.state: tuple[int,int,int,int]=(0x67452301,0xefcdab89,0x98badcfe,0x10325476)
        self.n_filled_bytes:int=0
        self.buf:bytearray=bytearray(64)
        pass

    def _step1(self, ):
        # Append Padding Bits to Message
        # TODO

        pass

    def _step2(self, ):
        # Append Length of Original Message
        # TODO
        pass

    def _step3(self, ):
        # Initialize MD Buffer
        # TODO
        pass

    def _step4(self, ):
        # Process Padded Message
        # TODO
        pass

    def _step5(self, ):
        # Output
        # TODO
        pass

    def __call__(self, data_to_digest):
        # Implements the algorithm by calling each _step* function
        print('result', data_to_digest)
