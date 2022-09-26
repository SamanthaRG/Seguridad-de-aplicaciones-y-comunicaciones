from ast import arg


class MD5:

    def __init__(self):
        # Initialize buffers, etc.
        # TODO
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
