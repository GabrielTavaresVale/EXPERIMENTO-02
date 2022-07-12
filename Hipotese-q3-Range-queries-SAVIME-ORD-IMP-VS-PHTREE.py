import numpy as np
from scipy import stats


sample=[788,755,696, 709, 673, 714, 692, 670, 743, 663]
pop_mean= 1052,3571
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
 





