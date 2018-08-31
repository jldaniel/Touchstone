from touchstone import Model
from numpy import array, exp, pi, cos


class Langermann(Model):
    def __init__(self):
        """
        Langermann Function m=5
        https://arxiv.org/pdf/1308.4008v1.pdf
        """
        super().__init__(name='Langermann')
        self._n_dim = 2
        self._x_opt = [2.00299219, 1.006096]
        self._f_opt = -5.1621259
        self._bounds = array([[0.0, 10.0], [0.0, 10.0]])

        self.a = [3, 5, 2, 1, 7]
        self.b = [5, 2, 1, 4, 9]
        self.c = [1, 2, 5, 2, 3]

    def evaluate(self, X):
        return -sum(self.c*exp(-(1/pi)*(pow(X[0] - self.a, 2.) + pow(X[1] - self.b, 2.))) *
                    cos(pi*(pow(X[0] - self.a, 2.) + pow(X[1] - self.b, 2.))))
