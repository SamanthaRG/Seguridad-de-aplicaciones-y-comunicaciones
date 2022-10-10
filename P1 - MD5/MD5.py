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
        """
        Inicializamos los buffers.
        """
        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0

        self.length: int = 0
        self.n_filled_bytes: int = 0
        self.buf: bytearray = bytearray(64)
        pass

    def _step1(self, msgOriginal):
        """
        Añadir bits de relleno al mensasje.
        :param msgOriginal: mensaje original que cifraremos
        :return: retorna el mensaje transformado en bits
        """

        # Codificamos el mensaje de entrada en bits.
        msgBits = bytearray(msgOriginal.encode('utf-8'))
        msgBits.append(0x80)

        # Comprobamos que la longitud del mensaje sea menor que 56 bytes para añadir tantos 0 como sean necesarios hasta que sea igual a 56.
        while (len(msgBits) % 64) < 56:
            msgBits.append(0)
        print(msgBits.hex())

        return msgBits

    def _step2(self, msgOriginal, msgBits):
        """
        Agregar longitud del mensaje original.
        ORIG LEN MOD64 -- 56, MSG+LEN
        :param msgOriginal: El mensaje que se introduce.
        :param msgBits: El mensaje que hemos transformado.
        :return: devuelve la suma en hexadecimal del mensaje
        """

        # Obtenemos la longitud del mensaje original.
        msgLen = len(msgOriginal)

        # Multiplicamos la longitud del mensaje original x8 para tener el mensaje en bytes.
        # Si el mensaje fuera muy grande -> (len(msg)*8)%(1<<64))
        mod64 = msgLen*8

        print(mod64)

        # Sumamos el mensaje original a la longitud calculada a bytes.
        sumaMod = msgBits+mod64.to_bytes(8, byteorder='little')
        print(sumaMod.hex())

        return sumaMod


    def _step3(self):
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
        msgBits = self._step1(data_to_digest)
        sumaMod = self._step2(data_to_digest, msgBits)

        print('result', data_to_digest)


if __name__ == '__main__':
    import argparse

    argp = argparse.ArgumentParser()
    argp.add_argument('instr', type=str)

    args = argp.parse_args()
    md5 = MD5()
    md5(args.instr)
