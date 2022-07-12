import numpy as np
from scipy import stats


sample=[646.03800,644.814, 668.55,646.518,647.194,655.537,644.716,645.138,644.312,800.066]
pop_mean= 1182,4
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
 





