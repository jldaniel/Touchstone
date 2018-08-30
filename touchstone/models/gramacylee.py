
from touchstone import Model
from numpy import array, sin, pi, power


class GramacyLee(Model):
    def __init__(self):
        super().__init__()
        self._n_dim = 1
        self._x_opt = [.5]
        self._y_opt = 0
        self._bounds = array([(0.5, 2.5)])

    def evaluate(self, X):
        y = sin(10*pi*X) / (2*X) + power(X - 1., 4.)
        return y