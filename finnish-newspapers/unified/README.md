
Unified data for Finnish newspapers:

 * [censorship_events.csv](censorship_events.csv): Censorship events affecting newspapers from 1800-> 1920 by Jani Marjanen based on Leino-Kaukiainen: Sensuuri ja sananvapaus Suomessa (1980).
 * [finnish_municipalities.csv](finnish_municipalities.csv): Finnish municipalities and their geocoordinates from [aggregation based on Wikipedia](http://datajournalismi.blogspot.fi/2013/03/suomen-kuntien-koordinaattitiedot.html) and updated with data from Google Maps for the municipalities in modern Russia.
 * [circulation_1800-1860.csv](circulation_1800-1860.csv): Circulation data from Tommila: Suomen lehdistön levikki ennen vuotta 1860 (1963), with estimates for select years added by Jani Marjanen.
   * start year,end year (both with .5 year precision),name,description
 * [issuedates.csv](issuedates.csv): Every published issue in 1771-1910, with issn, date, note and wordcount. Note refers to estimated date when the data was missing in the original. D is for estimated day and MD for estimated month and day. Generated with [src/publication_interval_data.py](src/publication_interval_data.py) from data downloaded from Kielipankki version of the Newspaper corpus via the KORP API.
