
Unified data for Finnish newspapers:

  * [censorship_events.csv](censorship_events.csv): Censorship events affecting newspapers from 1800-> 1920 by Jani Marjanen based on Leino-Kaukiainen: Sensuuri ja sananvapaus Suomessa (1980).
    * start year,end year (both with .5 year precision),name,description
 * [finnish_municipalities.csv](finnish_municipalities.csv): Finnish municipalities and their geocoordinates from [aggregation based on Wikipedia](http://datajournalismi.blogspot.fi/2013/03/suomen-kuntien-koordinaattitiedot.html) and updated with data from Google Maps for the municipalities in modern Russia.
 * [circulation_1800-1860.csv](circulation_1800-1860.csv): Circulation data from Tommila: Suomen lehdistön levikki ennen vuotta 1860 (1963), with estimates for select years added by Jani Marjanen. 
   * ISSN, year, circulation, source, qualifier (certain,approximate,partial,???) 
   * created with the following mutations from original CSV:
     * data2 = data %>% select(ISSN,16:76) %>% gather(year,circulation,2:62) %>% mutate(year,year=as.numeric(str_sub(year,9)))
     * data3 = data2 %>% mutate(source = NA, source = str_match(circulation, "([a-z]+)")[,1], circulation = as.numeric(str_match(circulation, "([0-9]+)")[,1]))
     * data4 = data3 %>% mutate(qualifier=case_when(.$source=="tap" ~ "partial", .$source=="ca" ~ "approximate", .$source=="ta" ~ "approximate", .$source=="pt" ~ "certain"), source=case_when(.$source=="pt" ~ "Päiviö Tommila", .$source=="tap" ~ "Päiviö Tommila", .$source=="ta" ~ "Päiviö Tommila", .$source=="ca" ~ "COMHIS collective"))
 * [issuedates.csv](issuedates.csv): Every published issue in 1771-1910, with issn, date, note and wordcount. Note refers to estimated date when the data was missing in the original. D is for estimated day and MD for estimated month and day. Generated with [src/publication_interval_data.py](src/publication_interval_data.py) from data downloaded from Kielipankki version of the Newspaper corpus via the KORP API.
 * [political_affiliations.csv](1905newspapers_parties.csv): Party affiliations for newspapers in 1905. Data provided by [Risto Turunen](http://www.uta.fi/yky/en/contact/personnel/ristoturunen). A newspaper may have multiple affiliations.
   * issn,affiliation,year
  * [circulation-utf8.csv](circulation-utf8.csv): Circulation data gathered by Finnish National Library, mainly based on Suomen lehdistön historia (1985-1992).
  * [circulation_areas-utf8.csv](circulation_areas-utf8.csv): Circulation locations data provided by Finnish National Library.
  * [publication_locations-utf8.csv](publication_locations-utf8.csv): Newspaper publication location data provided by Finnish National Library.
  * [newspapers-utf8.csv](newspapers-utf8.csv): Newspaper bibliographic metadata provided by Finnish National Library.
    * ISSN,TIETOLAHDE,P_ARTIKKELI,PAANIMEKE,M_ARTIKKELI,MUUNIMEKETIETO,AINYLEISMAARE,SANOMALEHTILUOKKA,JULKAISUMAA,KIELI,KOKOELMALAJI,KOKOELMA,VARASTOSIGNUM,KOKO,KORKEUS_CM,LEVEYS_CM,EKORKEUS,ESIVALMISTELUKUVAUS,KUSTANTAJA,JULKAISIJA,ILM_ALPVM,ILM_ALPVM_EPATARKKA,ILM_ALPVM_SUL,ILM_LOPVM,ILM_LOPVM_EPATARKKA,ILM_LOPVM_SUL,JULKAJAN_LISAMAARE,HIST_ALPVM,HIST_ALPVM_EPATARKKA,HIST_ALPVM_SUL,SARJAN_ISSN,S_ARTIKKELI,SARJAN_PAANIMEKE,SM_ARTIKKELI,SARJAN_MUU_NIMEKETIETO,SARJAN_TEKIJA,SARJAN_SIS_NUMEROINTI,A_ARTIKKELI,ALKUKIEL_JULK,PAAJULKAISUN_ISSN,PJ_ARTIKKELI,PAAJULKAISUN_NIMI,HUOMAUTUSKENTTA,TEKSTITYYPPI,HIST_LOPVM,HIST_LOPVM_EPATARKKA,HIST_LOPVM_SUL,FENNICA_ILMLOPVM (what are these?)

