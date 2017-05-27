[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> 34.27% of the population falls in the range of 5'10"-6'1"


```python
import scipy.stats
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
h1 = 5*30.48 + 10*2.54
h2 = 6*30.48 + 1*2.54
p = dist.cdf(h2) - dist.cdf(h1) # 0.34274683763147368
```
