__author__ = 'uwe'

from os import system

months = ['201207']
days   = list(range(1, 32, 1))
print(days)

for month in months:
    for day in days:
        _day = month + str(day).zfill(2)
        command = "python /home/uwe/cronjobs/nasa/modis/seadas_processing/GEO/create_MODIS_GEO_L1A_extract.py " + _day
        _ret = system(command)
        
