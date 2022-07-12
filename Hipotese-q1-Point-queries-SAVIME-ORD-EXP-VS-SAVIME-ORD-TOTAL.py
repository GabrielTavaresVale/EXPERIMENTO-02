import numpy as np
from scipy import stats


sample=[4589,4554,4342,4428,3809,3856,3829,3803,3811,3827]
pop_mean= 4389,6
mean= np.mean(sample)

std_error= np.std(sample) / np.sqrt(len(sample))

t= abs(mean-pop_mean) / std_error
print('t static:',t)

t_crit= stats.t.ppf(q=0.975, df= 9)
print("Critical value for t two tailed:",t_crit)


t_crit = stats.t.ppf(q=0.95, df=9)
print("Critical value for t one tailed:",t_crit)

p_value = (1-stats.t.cdf(x=t, df=9))

print("p-value:",p_value)
 





