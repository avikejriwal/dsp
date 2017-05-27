[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> the mean difference for the two groups is -0.125 lbs, indicating that the first babies are lighter than the others.  
>> Cohen's D between these two groups is -0.089.  While larger than the effect size for the difference in pregnancy length (0.0289), it is still quite small.

```python
CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
# -0.088672927072602006

CohenEffectSize(firsts.prglngth, others.prglngth)
# .028879044654449883
```

```python
def CohenEffectSize(group1, group2):
    """Computes Cohen's effect size for two groups.

    group1: Series or DataFrame
    group2: Series or DataFrame

    returns: float if the arguments are Series;
             Series if the arguments are DataFrames
    """
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / np.sqrt(pooled_var)
    return d

```
