# Getting Started
Run $ pip install -r requirements.txt in your virtual environment.

To see moneyball_functions.py open it with your text editor, the functions are support functions meant to be called by moneyball.ipynb.

To get to the main data open ipython notebook with $ ipython notebook and select `moneyball`.

In order for the data to be found there needs to be a directory named 'data' in the same directory as moneyball.ipynb.  In 'data' you should put the unzipped baseball stats files from http://www.seanlahman.com/baseball-archive/statistics/.  The files used for testing were the 2014 data.  They need to be the comma-delimited versions and should not be nested any deeper than in the data directory.

## Description
The ipython notebook moneyball.ipynb is a collection of functions that will import data from the baseball statistics folders and attempt to make the best team it can with players that have good on-base-percentage compared to their cost.  The salary data is good from 1985 to 2014, attempting to find further back with not return any results.  All data is from North American Major League Baseball.
