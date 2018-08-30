from touchstone import Model
from numpy import array, sin, exp, fabs, sqrt, pi


class CrossInTray(Model):
    def __init__(self):
        """
        Bukin Function N. 6
        https://www.sfu.ca/~ssurjano/bukin6.html

        Global Optimization Test Functions Index. Retrieved June 2013,
        from http://infinity77.net/global_optimization/test_functions.html#test-functions-index
        """
        super().__init__()
        self._n_dim = 2
        self._x_opt = [[1.3491, -1.3491], [1.3491, 1.3491], [-1.3491, 1.3491], [-1.3491, -1.3491]]
        self._f_opt = -2.06261
        self._bounds = array([[-10., 10.], [-10., 10.]])

    def evaluate(self, X):
        f1 = sin(X[0])*sin(X[1])
        print(repr(f1))
        f2 = exp(fabs(100. - sqrt(pow(X[0], 2.) + pow(X[1], 2.))/pi))
        print(repr(f2))
        return -0.0001*pow(fabs(f1 + f2) + 1., 0.1)


if __name__ == '__main__':
    X = [[-7.90666785, 1.20018952]]
    model = CrossInTray()
    model(X)

