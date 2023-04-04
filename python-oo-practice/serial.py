"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(seed=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, seed):
        '''initialize starting value'''
        self.seed = seed
        self.current = seed
        

    def generate(self):
        '''return current value and increment state'''
        val = self.current
        self.current += 1
        return val

    def reset(self):
        '''reset to starting value'''
        self.current = self.seed
        




    
