from ast import arg
from audioop import add
from calendar import c
from re import A





class MD5:

    def __init__(self):
        """
        Inicializamos los buffers.
        """
        A = 0x67452301
        B = 0xefcdab89
        C = 0x98badcfe
        D = 0x10325476

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

        return [self.A,self.B,self.C,self.D]

    def _step4(self, sumaMod):
        # TODO. Falta acabar 
        As=self._step3()

        def F(X, Y, Z):
            return (X & Y) | (~X & Z)
        def G(X, Y, Z):
            return (X & Z) | (Y & ~Z)
        def H(X, Y, Z):
            return X ^ Y ^ Z
        def I(X, Y, Z):
            return Y ^ (X | ~Z)

        def addmod(x, y =(1<<32)): #2^32
            return (x + y) % pow(2,32)

        def leftrotate(x,s):
            return (x << s) | (x >> (32 - s))

        K = [ 0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
        0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
        0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
        0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
        0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
        0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
        0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
        0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
        0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
        0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
        0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
        0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
        0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
        0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
        0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
        0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391 ]

        A=As[0]
        B=As[1]
        C=As[2]
        D=As[3]
        

        # PER CADA BLOC DE 64B:
        print(len(sumaMod))
        for i in range (0, len(sumaMod), 64):

            #FER MINI BLOCS DE 16b
            separacio = sumaMod[i : i + 64]
            print("separació: ", separacio)

            AA=A
            BB=B
            CC=C
            DD=D
            
            i=0
            for i in range(64):
                if 0 <= i <= 15:
                    func = F(B, C, D)
                    g = i
                    s = [7, 12, 17, 22]
                elif 16 <= i <= 31:
                    func = G(B, C, D)
                    g = (5 * i + 1) % 16
                    s = [5, 9, 14, 20]
                elif 32 <= i <= 47:
                    func = H(B, C, D)
                    g = (3 * i + 5) % 16
                    s = [4, 11, 16, 23] # M[g] must be a 32-bits block
                elif 48 <= i <= 63:
                    func = I(B, C, D)
                    g = (7 * i) % 16
                    s = [6, 10, 15, 21]
                
                func = addmod(func, addmod(A, addmod(K[i], int.from_bytes(separacio[4*g : 4*g+4], byteorder='little'))))
                A = D
                D = C
                C = B
                B = addmod(B, leftrotate(func, s[i % 4]))   

                print("STEP 4 -- MESSAGE CHUNK 0 -- Iteration",i,"-- BUFFERS AS INTS --('AA',",A,"),('BB',",B,"),('CC',",C,"),('DD',",D,"))")

            A=addmod(A,AA)
            B=addmod(B,BB)
            C=addmod(C,CC)
            D=addmod(D,DD)

            print("STEP 4 -- MESSAGE CHUNK 0 -- ACCUM BUFFERS -- ('A',",A,"),('B',",B,"),('C',",C,"),('D',",D,")")

        return A,B,C,D

    def _step5(self,A,B,C,D):
        # Output
        # TODO
        def swap32(x):
            return (((x << 24) & 0xFF000000) |#Movemos el byte 0 hasta el byte 3
                ((x <<  8) & 0x00FF0000) | #Movemos el byte 1 haste el byte 2
                ((x >>  8) & 0x0000FF00) | # Movemos el byte 2 hasta el byte 1
                ((x >> 24) & 0x000000FF)) #Movemos el byte 3 hasta el byte 0
        A=(swap32(A))
        B=(swap32(B))
        C=(swap32(C))
        D=(swap32(D))
        print("STEP 5 -- EACH BUFFER AS HEX -- ",f"{format(A, '08x')},{format(B, '08x')},{format(C, '08x')},{format(D, '08x')}")
        
        print ("== MD5 -- FINAL RESULT",f"{format(A, '08x')}{format(B, '08x')}{format(C, '08x')}{format(D, '08x')}")
        pass

    def __call__(self, data_to_digest):
        # Implements the algorithm by calling each _step* function
        msgBits = self._step1(data_to_digest)
        sumaMod = self._step2(data_to_digest, msgBits)
        self._step3()
        A,B,C,D=self._step4(sumaMod)
        self._step5(A,B,C,D)

        print('result', data_to_digest)


if __name__ == '__main__':
    import argparse

    argp = argparse.ArgumentParser()
    argp.add_argument('instr', type=str)

    args = argp.parse_args()
    md5 = MD5()
    md5(args.instr)
