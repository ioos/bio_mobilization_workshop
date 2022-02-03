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

Now that you know what the mapping is between your raw data and the Darwin Core standard, it's time to start cleaning up the data to align with the conventions described in the standard. The following activities are the three most common conversions a dataset will undergo to align to the Darwin Core standard. This includes:
1. Ensuring dates follow the [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) standard,
2. Matching scientific names to an authoritative resource,
3. Ensuring Latitude and Longitude values are in decimal degrees (with North and East as positive values). 

Below is a short summary of each of those conversions as well as some example conversion scripts. The exercises are intended to give you a sense of the variability we've seen in datasets and how we went about converting them.


# Getting your dates in order

> ## Example
> 
> Challenge: Convert the following dates to [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601).
> 
> 1. 01/31/2021 17:00 GMT
> 2. 31/01/2021 12:00 EST
> 3. January, 01 2021 5:00 PM GMT
> 4. noon Jan 01, 2021 EST 
> 5. 1612112400
> 6. 44227.70833
> 7. 2021-01-30 to 2021-01-31
> 
> > ## Solution
> > 1. ```python
> >    import pandas as pd
> >    date_str = '01/31/2021 17:00 GMT'
> >    date = pd.to_datetime(date_str, format="%m/%d/%Y %H:%M %Z").tz_convert(tz="UTC")
> >    print(date)
> >    ```
> >    ```output
> >    Timestamp('2021-01-31 17:00:00+0000', tz='GMT')
> >    ``` 
> >    ```r
> >    library(lubridate)
> >    date_str <- '01/31/2021 17:00 GMT'
> >    lubridate::mdy_hm(date_str,tz="UTC")
> >    ```
> >    ```output
> >    [1] "2021-01-31 17:00:00 UTC"
> >    ```
> > 2. ```python
> >    import pandas as pd
> >    date_str = '31/01/2021 12:00 EST'
> >    date = pd.to_datetime(date_str, format="%d/%m/%Y %H:%M %Z").tz_convert(tz="UTC")
> >    print(date)
> >    ```
> >    ```output
> >    Timestamp('2021-01-31 17:00:00+0000', tz='UTC')
> >    ``` 
> >    ```r
> >    library(lubridate)
> >    date_str <- '31/01/2021 12:00 EST'
> >    date <- lubridate::dmy_hm(date_str,tz="EST")
> >    lubridate::with_tz(date,tz="UTC")
> >    ```
> >    ```output
> >    [1] "2021-01-31 17:00:00 UTC"
> >    ```
> > 3. 2021-01-31T1700Z (note AM/PM)
> > 4. 2021-01-31T1700Z (note timezone and time in text)
> > 5. 2021-01-31T1700Z (was in seconds since 1970)
> > 6. 2021-01-31T1700Z (was an Excel date value)
> > 7. 2021-01-30/2021-01-31 (date ranges are represented)
> >
> > {: .output}
> {: .solution}
{: .challenge}

# Matching your scientific names to WoRMS
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

To note, latitude and longitude data pulled from OBIS into GBIF will be assumed to be in the geodetic datum `WGS84`. 
We highly recommend checking the coordinate reference system of your observations to confirm they are using the same 
datum. If your coordinates are not using `WGS84`, we highly recommend converting the coordinates to 

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
