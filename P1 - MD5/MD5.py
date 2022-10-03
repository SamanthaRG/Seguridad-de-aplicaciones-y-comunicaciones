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
        self.length: int = 0
        self.n_filled_bytes: int = 0
        self.buf: bytearray = bytearray(64)
        pass

    def _step1(self, msgOriginal):
        # Append Padding Bits to Message
        msgBits = bytearray(msgOriginal.encode('utf-8'))
        msgBits.append(0x80)

        while (len(msgBits) % 64) < 56:
            msgBits.append(0)

        print(msgBits.hex())
        pass

    def _step2(self, ):
        # Append Length of Original Message

        pass

    def _step3(self, ):
        # Initialize MD Buffer
        # self.state: tuple[int, int, int, int] = (0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476)
        self.A = 0x67452301
        self.B = 0xefcdab89
        self.C = 0x98badcfe
        self.D = 0x10325476
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
        self._step1(data_to_digest)
        print('result', data_to_digest)


if __name__ == '__main__':
    import argparse

    argp = argparse.ArgumentParser()
    argp.add_argument('instr', type=str)

    args = argp.parse_args()
    md5 = MD5()
    md5(args.instr)
