---
title: "QA/QC"
teaching: 0
exercises: 120
questions:
- "How can I QC and publish my data?"
objectives:
- "Data enhancement and quality control"
keypoints:
- "Several packages (e.g. obistools, Hmisc) can be used to QA/QC data." 
---

# Data enhancement and quality control

OBIS performs a number of quality checks on the data it receives. Red quality flags are attached to occurrence records if errors are encountered, and records may also be rejected if they do not meet minimum requirements. The checks that OBIS performs are documented [here](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4309024/pdf/bau125.pdf) and a python implementation is available [here](https://github.com/iobis/obis-qc). Therefore, prior to publishing your data to OBIS and/or GBIF, it is important to perform quality control on your standardized data. This can help identify any outliers or "faulty" data. It will also help with ensuring that your data is compatible and interoperable with other datasets published to OBIS. There are numerous functions within the [obistools](https://github.com/iobis/obistools) R packages that can serve to identify outliers, inspect quality or ensure that the dataset structure fits the required format for both the Event and Occurrence tables. 

> ## Recommended initial checks on your data
> * Make a map from your data to ensure the coordinates are valid and within your expected range.
> * Run basic statistics on each column of numeric data (min, max, mean, std. dev., etc.) to identify potential issues.
> * Look at unique values of columns containing string entries to identify potential issues (mainly spelling). 
> * Check for uniqueness of `occurrenceID` field.
> * Check for uniqueness of `eventID` for each event, if applicable. 
> * If recording `depth`, check the values are within your expected range.
> * _(optional)_ Check that the `scientificNameID` is/are valid. 
{: .callout}

One method for reviewing your data is to use the r package [Hmisc](https://cran.r-project.org/web/packages/Hmisc/index.html) and the function [describe](https://rdrr.io/cran/Hmisc/man/describe.html). Expand the example below using output from [this notebook](https://github.com/ioos/bio_data_guide/blob/main/datasets/TPWD_HARC_BagSeine/TPWD_HARC_BagSeine_OBISENV.md) to see how it works.

> ## Hmisc::describe
> ```r
> Hmisc::describe(occurrence)
> ```
> ```output
> occurrence 
> 18  Variables      202860  Observations
> -------------------------------------------------------------------------------------------------------
> vernacularName 
>        n  missing distinct 
>   202860        0       84 
>   
> lowest : Alligator gar        Arrow shrimp         Atlantic brief squid Atlantic croaker     Atlantic needlefish 
> highest: Thinstripe hermit    Threadfin shad       Tidewater silverside White mullet         White shrimp        
> -------------------------------------------------------------------------------------------------------
> eventID 
>        n  missing distinct 
>   202860        0     2415 
>
> lowest : Station_100_Date_03MAY1990:10:09:00.000 Station_100_Date_04NOV2008:07:15:00.000 Station_100_Date_04OCT2006:09:18:00.000 Station_100_Date_07APR1981:07:30:00.000
> Station_100_Date_07AUG1979:07:50:00.000
> highest: Station_99_Date_17SEP2002:09:25:00.000  Station_99_Date_20APR1999:10:08:00.000  Station_99_Date_22SEP1988:09:52:00.000  Station_99_Date_23MAY1996:07:10:00.000 
> Station_99_Date_29MAY1985:09:20:00.000 
> -------------------------------------------------------------------------------------------------------
> occurrenceStatus 
>        n  missing distinct
>   202860        0        2 
>                        
>   Value       Absent Present
>   Frequency   184636   18224
>   Proportion    0.91    0.09
> -------------------------------------------------------------------------------------------------------
> basisOfRecord 
>            n          missing         distinct            value 
>       202860                0                1 HumanObservation 
>                           
> Value      HumanObservation
> Frequency            202860
> Proportion                1
> -------------------------------------------------------------------------------------------------------
> scientificName 
>      n  missing distinct 
> 202860        0       84 
> 
> lowest : Achirus lineatus            Alpheus estuariensis        Anchoa mitchilli            Archosargus probatocephalus Argopecten irradians       
> highest: Syngnathus scovelli         Synodus foetens             Tozeuma carolinense         Trachinotus carolinus       Trinectes maculatus        
> -------------------------------------------------------------------------------------------------------
> scientificNameID 
>      n  missing distinct 
> 202860        0       84 
> 
> lowest : urn:lsid:marinespecies.org:taxname:107032 urn:lsid:marinespecies.org:taxname:107335 urn:lsid:marinespecies.org:taxname:107379
> urn:lsid:marinespecies.org:taxname:126430 urn:lsid:marinespecies.org:taxname:126803
> highest: urn:lsid:marinespecies.org:taxname:421735 urn:lsid:marinespecies.org:taxname:421784 urn:lsid:marinespecies.org:taxname:422069
> urn:lsid:marinespecies.org:taxname:443955 urn:lsid:marinespecies.org:taxname:581423
> -------------------------------------------------------------------------------------------------------
> kingdom 
>      n  missing distinct    value 
> 202860        0        1 Animalia 
>                    
> Value      Animalia
> Frequency    202860
> Proportion        1
> -------------------------------------------------------------------------------------------------------
> phylum 
>      n  missing distinct 
> 198030     4830        4 
>                                                      
> Value      Arthropoda   Chordata   Cnidaria   Mollusca
> Frequency       33810     149730       2415      12075
> Proportion      0.171      0.756      0.012      0.061
> -------------------------------------------------------------------------------------------------------
> class 
>      n  missing distinct 
> 198030     4830        7 
> 
> lowest : Actinopteri    Bivalvia       Cephalopoda    Elasmobranchii Gastropoda    
> highest: Cephalopoda    Elasmobranchii Gastropoda     Malacostraca   Scyphozoa     
>                                                                                                     
> Value         Actinopteri       Bivalvia    Cephalopoda Elasmobranchii     Gastropoda   Malacostraca
> Frequency          144900           4830           2415           4830           4830          33810
> Proportion          0.732          0.024          0.012          0.024          0.024          0.171
>                          
> Value           Scyphozoa
> Frequency            2415
> Proportion          0.012
> -------------------------------------------------------------------------------------------------------
> order 
>      n  missing distinct 
> 198030     4830       28 
> 
> lowest : [unassigned] Caenogastropoda Acanthuriformes              Aplysiida                    Atheriniformes               Aulopiformes                
> highest: Rhizostomeae                 Siluriformes                 Syngnathiformes              Tetraodontiformes            Venerida                    
> -------------------------------------------------------------------------------------------------------
> family 
>      n  missing distinct 
> 198030     4830       48 
> 
> lowest : Achiridae      Alpheidae      Aplysiidae     Ariidae        Atherinopsidae
> highest: Stromateidae   Syngnathidae   Synodontidae   Tetraodontidae Triglidae     
> -------------------------------------------------------------------------------------------------------
> genus 
>      n  missing distinct 
> 198030     4830       66 
> 
> lowest : Achirus     Alpheus     Anchoa      Archosargus Argopecten 
> highest: Syngnathus  Synodus     Tozeuma     Trachinotus Trinectes  
> -------------------------------------------------------------------------------------------------------
> scientificNameAuthorship 
>      n  missing distinct 
> 198030     4830       66 
> 
> lowest : (Baird & Girard, 1853)        (Baird & Girard, 1855)        (Blainville, 1823)            (Bleeker, 1863)               (Bloch & Schneider, 1801)    
> highest: Rathbun, 1896                 Say, 1817 [in Say, 1817-1818] Shipp & Yerger, 1969          Valenciennes, 1836            Valenciennes, 1847           
> -------------------------------------------------------------------------------------------------------
> taxonRank
>       n  missing distinct 
>  202860        0        4 
>                                                        
> Value           Genus      Order    Species Subspecies
> Frequency        2415       2415     195615       2415
> Proportion      0.012      0.012      0.964      0.012
> -------------------------------------------------------------------------------------------------------
> organismQuantity 
>      n  missing distinct     Info     Mean      Gmd      .05      .10      .25      .50      .75 
> 202860        0     3265    0.246   0.0119  0.02296     0.00     0.00     0.00     0.00     0.00 
>    .90      .95 
>   0.00     0.05 
>   
> lowest : 0.000000000 0.001897533 0.001964637 0.002000000 0.002433090
> highest: 0.935779817 0.942307692 0.942857143 0.952380952 0.973684211
> -------------------------------------------------------------------------------------------------------
> organismQuantityType 
>            n            missing           distinct              value 
>       202860                  0                  1 Relative Abundance 
>                              
> Value      Relative Abundance
> Frequency              202860
> Proportion                  1
> -------------------------------------------------------------------------------------------------------
> occurrenceID 
>      n  missing distinct 
> 202860        0   202860 
> 
> lowest : Station_100_Date_03MAY1990:10:09:00.000_Achirus_lineatus            Station_100_Date_03MAY1990:10:09:00.000_Alpheus_estuariensis       
> Station_100_Date_03MAY1990:10:09:00.000_Anchoa_mitchilli            Station_100_Date_03MAY1990:10:09:00.000_Archosargus_probatocephalus
> Station_100_Date_03MAY1990:10:09:00.000_Argopecten_irradians       
> highest: Station_99_Date_29MAY1985:09:20:00.000_Syngnathus_scovelli          Station_99_Date_29MAY1985:09:20:00.000_Synodus_foetens             
> Station_99_Date_29MAY1985:09:20:00.000_Tozeuma_carolinense          Station_99_Date_29MAY1985:09:20:00.000_Trachinotus_carolinus      
> Station_99_Date_29MAY1985:09:20:00.000_Trinectes_maculatus         
> -------------------------------------------------------------------------------------------------------
> collectionCode 
>                     n                     missing                    distinct 
>                202860                           0                           1 
>                 value 
> Upper Laguna Madre Gill Net 
> 
> Value      Upper Laguna Madre Gill Net
> Frequency                       202860
> Proportion                           1
> ```
> 
{: .solution}

> ## Exercise 
>
> **Challenge:** Perform the following minimal quality assurance and control checks: 
> 
> 1. Run a diagnostics report for the data quality. 
> 1. Ensure that the eventIDs are unique. 
> 1. Make sure that the eventDates follow ISO-8601 standards. 
> 1. Determine whether reported depths are accurate. 
> 
> The event core data used in the checks below can be found in [this Excel file]({{ page.root }}/data/trawl_fish.xlsx).
> 
> > ## Solution in R
> > Install [obistools](https://github.com/iobis/obistools) R packages.
> > 
> > 1. Run a diagnostics report for the data quality
> > ```r
> > report <- obistools::report(trawl_fish)
> > report
> > ```
> > <img src="{{ page.root }}/fig/screenshot_obistools_report.png" alt="drawing" width="500"/>{: .image-with-shadow }
> >
> > 1. Check to make sure `eventID` are unique
> >    ```r
> >    eventid <- obistools::check_eventids(trawl_fish)
> >    head(eventid)
> >    ```
> >    ```output
> >    # A tibble: 6 x 4
> >     field         level   row message                                                    
> >     <chr>         <chr> <int> <chr>                                                      
> >     1 eventID       error     7 eventID IYS:GoA2019:Stn6:trawl is duplicated               
> >     2 eventID       error     8 eventID IYS:GoA2019:Stn6:trawl is duplicated               
> >     3 parentEventID error     1 parentEventID IYS:GoA2019:Stn1 has no corresponding eventID
> >     4 parentEventID error     2 parentEventID IYS:GoA2019:Stn2 has no corresponding eventID
> >     5 parentEventID error     3 parentEventID IYS:GoA2019:Stn3 has no corresponding eventID
> >     6 parentEventID error     4 parentEventID IYS:GoA2019:Stn4 has no corresponding eventID
> >    ```
> >    
> > 1. Check for proper `eventDate` to ensure they follow ISO 8601 standards:
> >     ```r
> >     eventDate <- obistools::check_eventdate(trawl_fish)
> >     print(eventDate)  
> >     ```
> >     ```output
> >     # A tibble: 3 x 4
> >      level   row field     message                                                       
> >      <chr> <int> <chr>     <chr>                                                         
> >     1 error    10 eventDate eventDate 2019-02-24T07u40 does not seem to be a valid date   
> >     2 error    13 eventDate eventDate 2019-02-25 11h25min does not seem to be a valid date
> >     3 error    15 eventDate eventDate 2019-26-2 does not seem to be a valid date    
> >     ```
> >
> > 1. From the report generated under exercise 1, you can already see that there's measurements made on land. This information can also be gathered by plotting the map separately or using the `check_onland()` or `check_depth()` functions in the [obistools](https://iobis.github.io/obistools/) package.    
> >     ```r
> >     depth <- obistools::check_depth(trawl_fish)
> >     onland <- obistools::check_onland(trawl_fish) # Gives the same output.           
> >     print(depth)  
> >     ```
> >     ```output
> >     # A tibble: 1 x 16
> >      eventID parentEventID eventDate  year month   day decimalLatitude decimalLongitude footprintWKT coordinateUncer~ minimumDepthInM~
> >      <chr>   <chr>         <chr>     <dbl> <dbl> <dbl>           <dbl>            <dbl> <chr>                   <dbl>            <dbl>
> >     1 IYS:Go~ IYS:GoA2019:~ 2019-02-~  2019     2    22            67.4            -140. LINESTRING ~            2313.                0
> >     # ... with 5 more variables: maximumDepthInMeters <dbl>, samplingProtocol <chr>, locality <chr>, locationID <chr>, type <chr>    
> >     ```    
> >  {: .output}
> {: .solution}
> > ## Solution in Python
> > First start with reading the data into a pandas dataFrame:
> > ```python
> > import pandas as pd
> > url = 'https://ioos.github.io/bio_mobilization_workshop/data/trawl_fish.xlsx'
> > df = pd.read_excel(url)
> > df['row'] = df.index.to_numpy()+1 # python starts at zero
> > ```
> > 
> > 1. Run a diagnostics report for the data quality (you will need [cartopy](https://scitools.org.uk/cartopy/docs/latest/) installed - install with `conda install cartopy`)
> >     ```python
> >     import cartopy.io.shapereader as shpreader
> >     import geopandas as gpd
> >     import shapely.geometry as sgeom
> >     from shapely.ops import unary_union
> >     from shapely.prepared import prep
> >     import matplotlib.pyplot as plt
> >     
> >     gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.decimalLongitude, df.decimalLatitude))
> >     
> >     land_shp_fname = shpreader.natural_earth(resolution='50m',
> >                                            category='physical', name='land')
> >     
> >     land_geom = unary_union(list(shpreader.Reader(land_shp_fname).geometries()))
> >     land = prep(land_geom)
> >     
> >     for index, row in gdf.iterrows():
> >         gdf.loc[index, 'on_land'] = land.contains(row.geometry)
> >    
> >     fig, axs = plt.subplots(ncols=1,nrows=2)
> >     # Make a map:
> >     xlim = ([gdf.total_bounds[0]-2,  gdf.total_bounds[2]+2])
> >     ylim = ([gdf.total_bounds[1]-2,  gdf.total_bounds[3]+2])
> >
> >     axs[0].set_xlim(xlim)
> >     axs[0].set_ylim(ylim)
> > 
> >     gpd.read_file(land_shp_fname).plot(ax=axs[0])
> >     
> >     gdf.loc[gdf['on_land']==False].plot(ax=axs[0], color='green', markersize=1)
> >     gdf.loc[gdf['on_land']==True].plot(ax=axs[0], color='red', markersize=1)
> >     
> >     # Collect some informational material about potential issues w/ data:
> >     invalid_coord = []
> >     if len(gdf.loc[gdf['on_land']==True]) > 0:
> >        invalid_coord.append('Row {} coordinates on land.'.format(gdf[gdf['on_land'] == True,'row']))
> >     
> >     req_cols = ['eventDate', 'decimalLongitude', 'decimalLatitude', 'scientificName', 'scientificNameID', 'occurrenceStatus', 'basisOfRecord']
> >     missing_cols = []
> >     for col in req_cols:
> >      if col not in gdf.columns:
> >        missing_cols.append('Column {} is missing.'.format(col))
> >     
> >     # Add the information to the figure
> >     axs[1].text(0.25,0.25,'\n'.join(['\n'.join(missing_cols),'\n'.join(invalid_coord)]))
> >     axs[1].axis('off')
> >     ```
> >     <img src="{{ page.root }}/fig/screenshot_python_report.png" alt="drawing" width="500"/>{: .image-with-shadow }
> > 1. Check to make sure `eventID` are unique
> >    ```python
> >    dup_events = df.loc[df['eventID'].duplicated()]
> >    print('Duplicated eventID:\n',dup_events[['eventID','row']])
> >    
> >    parent_not_event = df.loc[~df['eventID'].isin(df['parentEventID'].unique())]
> >    print('\nparentEventID missing corresponding eventID:\n', parent_not_event[['parentEventID','row']])
> >    ```
> >    ```output
> >    Duplicated eventID:
> >                       eventID  row
> >    6  IYS:GoA2019:Stn6:trawl    7
> >    7  IYS:GoA2019:Stn6:trawl    8
> >    
> >    parentEventID missing corresponding eventID:
> >             parentEventID  row
> >    0    IYS:GoA2019:Stn1    1
> >    1    IYS:GoA2019:Stn2    2
> >    2    IYS:GoA2019:Stn3    3
> >    3    IYS:GoA2019:Stn4    4
> >    4    IYS:GoA2019:Stn5    5
> >    ..                ...  ...
> >    59  IYS:GoA2019:Stn60   60
> >    60  IYS:GoA2019:Stn61   61
> >    61  IYS:GoA2019:Stn62   62
> >    62  IYS:GoA2019:Stn63   63
> >    63  IYS:GoA2019:Stn64   64
> >    [64 rows x 2 columns]
> >    ```
> >    
> > 1. Check for proper `eventDate` to ensure they follow ISO 8601 standards:
> >    ```python
> >    for date in df['eventDate']:
> >        try:
> >            pd.to_datetime(date)
> >        except:
> >            print("Date",date,"might not follow ISO 8601")
> >    ```
> >    
> > 1. From the report generated under exercise 1, you can already see that there’s measurements made on land. Now let's check the depths are within reason for the points. Let's use the [GEBCO bathymetry dataset served in the coastwatch ERDDAP](https://coastwatch.pfeg.noaa.gov/erddap/griddap/GEBCO_2020.html).
> >    ```python
> >    import time
> >    
> >    for index, row in df.iterrows():
> >        url = 'https://coastwatch.pfeg.noaa.gov/erddap/griddap/GEBCO_2020.csvp?elevation%5B({})%5D%5B({})%5D'.format(row['decimalLatitude'],row['decimalLongitude'])
> >        bathy = pd.read_csv(url)
> >        df.at[index,'bathy'] = bathy['elevation (m)'] # insert bathymetry value
> >        time.sleep(0.5) # to not ping erddap too much
> >    
> >    print('maximumDepthInMeters deeper than GEBCO bathymetry:')
> >    if len(df.loc[df['maximumDepthInMeters']<df['bathy']]) > 0:
> >       print(df.loc[df['maximumDepthInMeters']<df['bathy']])
> >    else:
> >       print('None')
> >    ```
> >    ```output
> >    max Depths > GEBCO bathymetry:
> >    None
> >    ```
> {: .solution}
{: .challenge}

{% include links.md %}
