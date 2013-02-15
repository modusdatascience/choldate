__author__ = 'jasonrudy'

import unittest
import numpy
from choldate import cholupdate, choldowndate



class TestCholdate(unittest.TestCase):
    
    def setUp(self):
        numpy.random.seed(1)
        self.X = numpy.random.normal(size=(100,10))
    
    def test_update(self):
        V = numpy.dot(self.X.transpose(),self.X)
        R = numpy.linalg.cholesky(V).transpose()
        u = numpy.random.normal(size=R.shape[0])
        V1 = V + numpy.outer(u,u)
        R1 = numpy.linalg.cholesky(V1).transpose()
        R_ = R.copy()
        u_ = u.copy()
        cholupdate(R_,u_)
        self.assertAlmostEqual(numpy.max((numpy.abs(R_) - numpy.abs(R1))**2),0)

    def test_downdate(self):
        V = numpy.dot(self.X.transpose(),self.X)
        R = numpy.linalg.cholesky(V).transpose()
        u = numpy.random.normal(size=R.shape[0])
        V1 = V + numpy.outer(u,u)
        R1 = numpy.linalg.cholesky(V1).transpose()
        R_ = R1.copy()
        u_ = u.copy()
        choldowndate(R_,u_)
        self.assertAlmostEqual(numpy.max((numpy.abs(R_) - numpy.abs(R))**2),0)


if __name__ == '__main__':
    unittest.main()
