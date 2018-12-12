"""
these are my data analysis functions 
used to download and process some temperature
time series from berkeley Earth.
"""

import numpy as np
import requests

def generate_url(location):
    #f allows you to replace things in the string, in this case the 'location' is put where it is in the string and we always want it lowercase
    url = f'http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/{location.lower()}-TAVG-Trend.txt'
    return url

def download_data(location):
    url = generate_url(location)
    # Download the content of the URL
    response = requests.get(url)
    # Save it to a file
    #with open("data.txt", 'w') as open_file:
    #    open_file.write(response.text)
        
    data = np.loadtxt(response.iter_lines(), comments="%") 
    
    return(data)

def moving_avg(data, width):
    """
    computes the moving average. 

    :param data: Input data array.
    :param width: width in samples.
    """
    moving_avg = np.full(data.size, np.nan)
    for i in range(width, data.size - width):
        moving_avg[i] = np.mean(data[i - width:i + width])
    return(moving_avg)