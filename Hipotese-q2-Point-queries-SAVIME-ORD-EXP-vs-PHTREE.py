import numpy as np
from scipy import stats


sample=[1376,1430,1623,1426,1444,1364,1407,1373,1463,1348]
pop_mean= 3703,1
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
 





