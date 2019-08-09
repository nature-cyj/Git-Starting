# class of van der pol oscillator

class Oscillator(object):
    """
    Physical osciallator
    """
    def __init__(self, m, w0, b):
        self.m = m
        self.w0 = w0
        self.b = b
    pass


class Van_der_pol(Oscillator):
    """
    Van der Pol Oscillator
    """
    def __init__(self, mu, theta_0):
        self.mu = mu
        self.theta_0 = theta_0

    pass
