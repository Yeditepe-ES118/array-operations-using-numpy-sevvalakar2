

import numpy as np

def stat():
   
    data = np.loadtxt('populations.txt')

   
    hare = data[:, 1]

    min_idx_hare = np.argmin(hare)
    min_year_hare = data[min_idx_hare, 0]

    
    lynx_avg = np.mean(data[:, 2])

  
    species_sum = np.sum(data[:, 1:], axis=1).reshape(-1, 1)
    new_data = np.hstack((data, species_sum))

    
    new_data[new_data[:, 3] < 40000, 3] = 0

   
    return data, hare, min_year_hare, lynx_avg, new_data