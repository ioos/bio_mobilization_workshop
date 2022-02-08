---
title: "Data Cleaning"
teaching: 0
exercises: 120
questions:
- "How do I clean my data?"
objectives:
- "Getting your dates in order."
- "Matching scientific names to WoRMS."
- "Getting latitude and longitude to decimal degrees."
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"
---

Now that you know what the mapping is between your raw data and the Darwin Core standard, it's time to start cleaning up 
the data to align with the conventions described in the standard. The following activities are the three most common 
conversions a dataset will undergo to align to the Darwin Core standard. This includes:
1. [Ensuring dates follow the ISO-8601 standard](#getting-your-dates-in-order)
2. [Matching scientific names to an authoritative resource](#matching-your-scientific-names-to-worms)
3. [Ensuring latitude and longitude values are in decimal degrees](#getting-latlon-to-decimal-degrees)

Below is a short summary of each of those conversions as well as some example conversion scripts. The exercises are 
intended to give you a sense of the variability we've seen in datasets and how we went about converting them. While the
examples use the [pandas package for Python](https://pandas.pydata.org/) and the [tidyverse collection of packages for R](https://www.tidyverse.org/), 
those are not the only options for managing these conversions. Simply the ones we recommend and use more frequently in 
our experiences. 


# Getting your dates in order
Dates can be surprisingly tricky because people record them in many different ways. For our purposes we must follow 
[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) which means using a four digit year, two digit month, and two digit 
day with dashes as separators (i.e. `YYYY-MM-DD`). You can also record time in ISO 8601 but make sure to include the time 
zone which can also get tricky if your data take place across time zones and throughout the year where daylight savings 
time may or may not be in effect (and start and end times of daylight savings vary across years). There are packages in 
R and Python that can help you with these vagaries. Finally, it is possible to record time intervals in ISO 8601 using a 
slash (e.g. `2022-01-02/2022-01-12`). Examine the dates in your data to determine what format they are following and what 
amendments need to be made to ensure they are following ISO 8601. Below are some examples and solutions in Python and R 
for them.

> ## Tip 
> Focus on getting your package of choice to read the dates appropriately. While you can use [regular expressions](https://en.wikipedia.org/wiki/Regular_expression)
> to replace and substitute strings to align with the ISO convention, it's typically more reusable and saves you time 
> if you work in your package of choice to translate the dates.
{: .callout}

> ## Examples
> 
> Converting the following dates to [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601).
> 
> 1. 01/31/2021 17:00 GMT
> 2. 31/01/2021 12:00 EST
> 3. January, 31 2021 5:00 PM GMT
> 5. 1612112400
> 6. 44227.708333333333
> 7. 2021-01-30 to 2021-01-31
> 
> > ## Solution (python)
> > When dealing with dates using pandas in Python it is best to create a Series as your time column with the appropriate 
> > datatype. Then, when writing your file using [.to_csv()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)
> > you can specify the format which your date will be written using the `date_format` parameter. 
> >
> > The examples below show how to use the [pandas.to_datetime](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html)
> > function to read various date formats. The process can be applied to entire columns (or Series) within a DataFrame.
> > 1. ```python
> >    import pandas as pd
> >    df = pd.DataFrame({'date':['01/31/2021 17:00 GMT']})
> >    df['eventDate'] = pd.to_datetime(df['date'], format="%m/%d/%Y %H:%M %Z")
> >    df
> >    ```
> >    ```output
> >                       date                 eventDate
> >    0  01/31/2021 17:00 GMT 2021-01-31 17:00:00+00:00
> >    ``` 
> > 2. ```python
> >    import pandas as pd
> >    df = pd.DataFrame({'date':['31/01/2021 12:00 EST']})
> >    df['eventDate'] = pd.to_datetime(df['date'], format="%d/%m/%Y %H:%M %Z")
> >    df
> >    ```
> >    ```output
> >                       date                 eventDate
> >    0  31/01/2021 12:00 EST 2021-01-31 12:00:00-05:00
> >    ``` 
> >    
> > 3. ```python
> >    import pandas as pd
> >    df = pd.DataFrame({'date':['January, 01 2021 5:00 PM GMT']})
> >    df['eventDate'] = pd.to_datetime(df['date'],format='%B, %d %Y %I:%M %p %Z')
> >    df
> >    ```
> >    ```output
> >                               date                 eventDate
> >    0  January, 01 2021 5:00 PM GMT 2021-01-01 17:00:00+00:00
> >    ```
> >    
> > 4. ```python
> >    import pandas as pd
> >    df = pd.DataFrame({'date':['1612112400']})
> >    df['eventDate'] = pd.to_datetime(df['date'], unit='s', origin='unix')
> >    df
> >    ```
> >    ```output
> >             date           eventDate
> >    0  1612112400 2021-01-31 17:00:00
> >    ```
> > 5. ```python
> >    import pandas as pd
> >    df = pd.DataFrame({'date':['44227.708333333333']})
> >    df['eventDate'] = pd.to_datetime(df['date'].astype(float), unit='D', origin='1899-12-30')
> >    df
> >    ```
> >    ```output
> >                     date                     eventDate
> >    0  44227.708333333333 2021-01-31 17:00:00.000000256
> >    ```
> > 6. ```python
> >    import pandas as pd
> >    df = pd.DataFrame({'start_date':['2021-01-30'],
> >                       'end_date':['2021-01-31']})
> >    df['eventDate'] = df['start_time']+'/'+df['end_time']
> >    df
> >    ```
> >    ```output
> >       start_time    end_time              eventDate
> >    0  2021-01-30  2021-01-31  2021-01-30/2021-01-31
> >    ```
> >
> > {: .output}
> {: .solution}
> > ## Solution (R)
> > 1.  ```r
> >    library(lubridate)
> >    date_str <- '01/31/2021 17:00 GMT'
> >    lubridate::mdy_hm(date_str,tz="UTC")
> >    ```
> >    ```output
> >    [1] "2021-01-31 17:00:00 UTC"
> >    ```
> > 2. ```r
> >    library(lubridate)
> >    date_str <- '31/01/2021 12:00 EST'
> >    date <- lubridate::dmy_hm(date_str,tz="EST")
> >    lubridate::with_tz(date,tz="UTC")
> >    ```
> >    ```output
> >    [1] "2021-01-31 17:00:00 UTC"
> >    ```
> > {: output}
> {: .solution}
{: .challenge}

# Matching your scientific names to WoRMS
OBIS uses the [World Register of Marine Species (WoRMS)](https://www.marinespecies.org/) as the taxonomic backbone for its system. GBIF uses the [Catalog of Life](https://www.catalogueoflife.org/). Since WoRMS contributes to the Catalog of Life and WoRMS is a requirement for OBIS we will teach you how to do your taxonomic lookups using WoRMS. The key Darwin Core terms that we need from WoRMS are `scientificNameID` also known as the WoRMS LSID which looks something like this "urn:lsid:marinespecies.org:taxname:105838" and `kindgom` but you can grab the other parts of the taxonomic hierarchy if you want as well as `taxonRank`. 

There are two ways to grab the taxonomic information necessary. First you can use the [WoRMS Taxon Match Tool](https://www.marinespecies.org/aphia.php?p=match). The tool accepts lists of scientific names (each unique name as a separate row in a .txt, .csv, or .xlsx file) up to 1500 names and provides an interface for selecting the match you want for ambiguous matches. A step by step guide on using WoRMS Taxa Match Tool for the MBON Pole to Pole found here: https://marinebon.org/p2p/protocols/WoRMS_quality_check.pdf (NOTE from Abby: the instructions are very specific to the mbon pole to pole data. I wonder if we rewrite this guide here in this page but more generically?)

The other way to get the taxonomic information you need is to use [worrms](https://cran.r-project.org/web/packages/worrms/worrms.pdf) or [pyworms](https://github.com/iobis/pyworms). 

(NOTE from Abby- I think we should remove this example challenge. I'm not sure it helps people with what to do. Instead some example lookups using worrms and pyworms seems like it would be better to have.)
> ## Example
> 
> Challenge: Match the following names to a taxonomic authority.
> 
> 1. White shark
> 
> > ## Solution
> > 1. [_Carcharodon carcharias_](https://www.marinespecies.org/aphia.php?p=taxdetails&id=105838)
> >    - AphiaID - `urn:lsid:marinespecies.org:taxname:105838`
> >
> > {: .output}
> {: .solution}
{: .challenge}



# Getting lat/lon to decimal degrees

Note, that the requirement for `decimalLatitude` and `decmailLongitude` is they must be in decimal degrees in WGS84. Since this is the requirement for Darwin Core, OBIS and GBIF will assume data shared using those Darwin Core terms are in the geodetic datum `WGS84`. We highly recommend checking the coordinate reference system of your observations to confirm they are using the same datum. If your coordinates are not using `WGS84`, they will need to be converted in order to share the data to OBIS and GBIF since `decimalLatitude` and `decimalLongitude` are required terms.

| Darwin Core Term | Description | Example |
|------------------|-------------|---------|
| [dwc:decimalLatitude](https://dwc.tdwg.org/list/#dwc_decimalLatitude) | The geographic latitude (in decimal degrees, using the spatial reference system given in geodeticDatum) of the geographic center of a Location. Positive values are north of the Equator, negative values are south of it. Legal values lie between -90 and 90, inclusive. | -41.0983423 |
| [dwc:decimalLongitude](https://dwc.tdwg.org/list/#dwc_decimalLongitude) | The geographic longitude (in decimal degrees, using the spatial reference system given in geodeticDatum) of the geographic center of a Location. Positive values are east of the Greenwich Meridian, negative values are west of it. Legal values lie between -180 and 180, inclusive. | -121.1761111 |

> ## Example
> 
> Challenge: Convert the following latitude and longitude values to decimal degrees north and east, respectively.
> 
> 1. `17° 51' 57.96" S` `149° 39' 13.32" W` 
> 2. `33° 22.967' N` `117° 35.321' W`
> 
> > ## Solution
> > 1. [Teahupoo, Tahiti](https://www.google.com/maps/search/?api=1&query=-17.8658056%2C-149.2560498)
> >    1. latitude = -17.8661 degrees north
> >    2. longitude = -149.6537 degrees east
> > 2. [Trestles, CA](https://www.google.com/maps/search/?api=1&query=33.3828%2C-117.5886)
> >    1. latitude = 33.3828 degrees north
> >    2. longitude = -117.5886 degrees east
>>
> > {: .output}
> {: .solution}
{: .challenge}

{% include links.md %}
