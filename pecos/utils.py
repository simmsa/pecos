"""
The utils module contains helper functions.
"""
import pandas as pd
import numpy as np
from pandas.tseries.frequencies import to_offset
import logging
import os

logger = logging.getLogger(__name__)
        
def round_index(dt, frequency, how='nearest'):
    """
    Round datetime index
    
    Parameters
    ----------
    dt : DatetimeIndex
        Time series index
    
    frequency : int
        Expected timeseries frequency, in seconds
    
    how : string (default = 'nearest')
        Method for rounding.  Options include:
        
        - nearest = round the index to the nearest expected integer
        - floor= round the index to the largest expected integer such that the integer <= index
        - ceiling = round the index to the smallest expected integer such that the integer >= index
        
    Returns
    -------
    rounded _dt : DatetimeIndex
        Rounded time series index
    """
    freq=str(frequency) + 's'
    freq = to_offset(freq).nanos
    
    if how=='nearest':
        rounded_dt = pd.DatetimeIndex(((np.round(dt.asi8/(float(freq)))*freq).astype(np.int64)))
    elif how=='floor':
        rounded_dt = pd.DatetimeIndex(((np.floor(dt.asi8/(float(freq)))*freq).astype(np.int64)))
    elif how=='ceiling':
        rounded_dt = pd.DatetimeIndex(((np.ceil(dt.asi8/(float(freq)))*freq).astype(np.int64)))
    else:
        logger.info("Invalid input, index not rounded")
        rounded_dt = dt

    return rounded_dt

def convert_html_to_image(html_filename, image_filename, image_format='jpg', quality=100, zoom=1):
    """
    Convert html file to impage file using wkhtmltoimage
    See http://wkhtmltopdf.org/ for more information
    
    Parameters
    ----------
    html_filename : string
        HTML filename with full path
    
    image_filename : string
        Image filename with full path
    
    image_format : string  (default = 'jpg')
        Image format
    
    quality : int (default = 100)
        Image quality 
    
    zoom : int (default = 1)
        Zoom factor
    """
    os.system('wkhtmltoimage --format ' + image_format + 
                           ' --quality ' + str(quality) + 
                           ' --zoom ' + str(zoom) + ' ' + 
                            html_filename + ' ' + image_filename)