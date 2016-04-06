choldate
========

Somewhat fast updating and downdating of Cholesky factors in Python

##installation

Install from GitHub: `pip install git+git://github.com/jcrudy/choldate.git`

Or, clone the GitHub repository and install from source, e.g.,

1. `git clone git://github.com/jcrudy/choldate.git`
2. `cd choldate; python setup.py install`

I am new to packaging Python modules.  If it doesn't work on your system, get in touch and I'll try to help you.

##usage
```python
from choldate import cholupdate, choldowndate
import numpy

#Create a random positive definite matrix, V
numpy.random.seed(1)
X = numpy.random.normal(size=(100,10))
V = numpy.dot(X.transpose(),X)

#Calculate the upper Cholesky factor, R
R = numpy.linalg.cholesky(V).transpose()

#Create a random update vector, u
u = numpy.random.normal(size=R.shape[0])

#Calculate the updated positive definite matrix, V1, and its Cholesky factor, R1
V1 = V + numpy.outer(u,u)
R1 = numpy.linalg.cholesky(V1).transpose()

#The following is equivalent to the above
R1_ = R.copy()
cholupdate(R1_,u.copy())
assert(numpy.all((R1 - R1_)**2 < 1e-16))

#And downdating is the inverse of updating
R_ = R1.copy()
choldowndate(R_,u.copy())
assert(numpy.all((R - R_)**2 < 1e-16))  
``` 
