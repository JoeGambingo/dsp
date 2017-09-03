[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> The distribution is incredibly uniform.  
Below is my code.

```
import thinkstats2
import random

random_sample = []
for ii in range(0, 1000):
    random_sample.append(random.random())

random_pmf = thinkstats2.Pmf(random_sample)
random_cdf = thinkstats2.Cdf(random_sample)

thinkplot.PrePlot(2, cols=2)
thinkplot.Pmf(random_pmf)
thinkplot.SubPlot(2)
thinkplot.Cdf(random_cdf)
thinkplot.Show()
```
