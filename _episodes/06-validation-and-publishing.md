---
title: "Metadata, validating, and publishing"
teaching: 0
exercises: 90
questions:
- "How can I QC and publish my data?"
objectives:
- "Compiling metadata for EML."
- "Data enhancement and quality control"
keypoints:
- "Some metadata fields in the Ecological Metadata Language (EML) are required for publishing to OBIS."
- "Several packages (e.g. obistools, Hmisc) can be used to QA/QC data." 
---

1. Creating EML metadata text file
2. Data enhancement and quality control

# Integrated Publishing Toolkit
The [GBIF Integrated Publishing Toolkit (IPT)](https://www.gbif.org/ipt) is currently the only way to publish data to OBIS. [OBIS nodes](https://obis.org/contact/) host an IPT instance for their region or theme. The [OBIS-USA IPT](https://www1.usgs.gov/obis-usa/ipt/) (hosted at the USGS) is available for anyone in the US to publish their data to OBIS and GBIF. To publish using this IPT work with the OBIS-USA node manager, Abby Benson. You can choose to download and install your own instance of the IPT but it might be difficult to register it with OBIS. Instead it's recommended to work with one of the OBIS nodes to publish your data through their IPT. The requirements for publishing via an OBIS node IPT are that the data follows Darwin Core, includes the required Darwin Core and EML metadata elements, and you have contacted the node to ensure the data are a good fit for that node. 

![screenshot]({{ page.root }}/fig/DwC_workflow.jpg){: .image-with-shadow }


# Ecological Metadata Language (EML) 

Both OBIS and GBIF use [Ecological Metadata Language (EML)](https://eml.ecoinformatics.org/) as the metadata standard associated with the data. For the purposes of this workshop we will not dive into the world of EML. However, we should note that when publishing your data through the IPT, the IPT helps you create an EML file as part of the Darwin Core Archive (DwC-A). As such, if you publish your own data through the IPT, there is no need for innate knowledge on the EML format. But there are a minimum required number of fields that would need to be filled out in the IPT: `title`, `abstract`, `citation`, and several `contacts`.

More information on EML can be found in the [bio data guide](https://ioos.github.io/bio_data_guide/extras.html#ecological-metadata-language-eml).

> ## Tip 
> Try to collect as much of this information as possible before and during the Darwin Core alignment process. It will 
> significantly reduce the amount of time it takes to load the data into the IPT.
{: .callout}

## Required EML metadata fields for sharing to OBIS

| EML Fields | Definition | Comment |
| ---------- | ---------- | ------- |
| `Title` | A good descriptive title is indispensable and can provide the user with valuable information, making the discovery of data easier. | The IPT requires you to provide a Shortname. Shortnames serve as an identifier for the resource within the IPT installation. Spell out acronyms in Title but they are ok to use in the shortname. |
| `Abstract`             | The abstract or description of a dataset provides basic information on the content of the dataset. The information in the abstract should improve understanding and interpretation of the data.                                |                                                                                                                                                                                      |
| `Data License`         | The licence that you apply to the resource. The license provides a standardized way to define appropriate uses of your work.                                                                                                   | Must use CC-0, CC-BY, or CC-BY-NC. Description of the licenses can be found [here](https://creativecommons.org/).                                                                                                                                                   |
| `Resource Contact(s)`  | The list of people and organizations that should be contacted to get more information about the resource, that curate the resource or to whom putative problems with the resource or its data should be addressed.             | Last name, Postition, and Organization are required, helpful to include an ORCID and a contact method like email or phone number.                                                                 |
| `Resource Creator(s)`  | The people and organizations who created the resource, in priority order. The list will be used to auto-generate the resource citation (if auto-generation is turned on).                                                      |                                                                                                                                                                                      |
| `Metadata Provider(s)` | the people and organizations responsible for producing the resource metadata.                                                                                                                                                  |                                                                                                                                                                                      |
| `Citation`             | The dataset citation allows users to properly cite the datasets in further publications or other uses of the data. The OBIS download function provides a list of the dataset citations packaged with the data in a zipped file. |                                                                                                                                                                                      |

## Other EML fields to consider

| EML Fields               | Definition | Comment |
|--------------------------|------------|---------|
| `Bounding Box`           | Fatherest North, South, East, and West coordinate. |  |
| `Geographic Description` | A textual description of the geographic coverage.  |  |
| `Temporal Coverage`      | This can either be a Single Date, Date Range, Formation Period, or Living Time Period. |  |
| `Study Extent`           | This field represents both a specific sampling area and the sampling frequency (temporal boundaries, frequency of occurrence) of the project. |  |
| `Sampling Description`   | This field allows for a text-based/human readable description of the sampling procedures used in the research project. | The content of this element would be similar to a description of sampling procedures found in the methods section of a journal article.  |
| `Step Description`       | This field allows for repeated sets of elements that document a series of methods and procedures used in the study, and the processing steps leading to the production of the data files. These include e.g. text descriptions of the procedures, relevant literature, software, instrumentation and any quality control measurements taken. | Each method should be described in enough detail to allow other researchers to interpret and repeat the study, if required. |

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

> ## Exercise 
>
> **Challenge:** Perform the following minimal quality assurance and control checks: 
> 
> 1. run a diagnostics report for the data quality, 
> 1. ensure that the eventIDs are unique, 
> 1. make sure that the eventDates follow ISO-8601 standards, and 
> 1. determine whether reported depths are accurate. 
> 
> The event core data used in the checks below can be found in [this Excel file]({{ page.root }}/data/trawl_fish.xlsx).
> 
> > ## Solution in R
> > Install [obistools](https://github.com/iobis/obistools) and [Hmisc](https://cran.r-project.org/web/packages/Hmisc/Hmisc.pdf) R packages.
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
