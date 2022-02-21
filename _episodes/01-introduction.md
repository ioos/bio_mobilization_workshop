---
title: "Introduction to Darwin Core"
start: true
teaching: 0
exercises: 90
questions:
- "What is Darwin Core?"
- "What is a Darwin Core Archive?"
- "Why do people use Darwin Core for their data?"
- "What are the required Darwin Core terms for sharing to OBIS?"
objectives:
- "Understand the purpose of Darwin Core."
- "Understand how to map data to Darwin Core."
- "Plan for mapping to Darwin Core."
keypoints:
- "Darwin Core isn't difficult to apply, it just takes a little bit of time."
- "Using Darwin Core allows datasets from across projects, organizations, and countries to be integrated together."
- "Applying certain general principles to the data will make it easier to map to Darwin Core."
- "Implementing Darwin Core makes data FAIR-er and means becoming part of a community of people working together to understand species no matter where they work or are based."
---
# Darwin Core - A global community of data sharing and integration
Darwin Core is a data standard to mobilize and share biodiversity data through well-established data repositories. Over the years, the Darwin Core standard has expanded to enable exchange and sharing of diverse types of biological observations from citizen scientist, ecological monitoring, eDNA, animal telemetry, taxonomic treatments, and many others. Darwin Core is applicable to any measurement of an organism (scientific name, OTU, or other methods of defining a species) at a particular place and time. In Darwin Core this is an `occurrence`. To learn more about the foundations of Darwin Core read [Wieczorek et al. 2012](https://doi.org/10.1371/journal.pone.0029715).

### Demonstrated Use of Darwin Core
The power of Darwin Core is most evident in the data aggregators that harvest data using that standard. The one we will refer to most frequently in this workshop is the [Ocean Biodiversity Information System](https://obis.org/) (learn more about [OBIS](https://youtu.be/E6NblAC-1uE)). Another prominent one is the [Global Biodiversity Information Facility](https://www.gbif.org/) (learn more about [GBIF](https://vimeo.com/434831655)). It's also used by the Atlas of Living Australia, iDigBio, among others. 

### Darwin Core Archives
Darwin Core Archives are what OBIS and GBIF harvest into their systems. Fortunately the software created and maintained by GBIF, the [Integrated Publishing Toolkit](https://www.gbif.org/ipt), produces Darwin Core Archives for us. Darwin Core Archives are pretty simple. It's a zipped folder containing the data (one or several files depending on how many extensions you use), an Ecological Metadata Language (EML) XML file, and a meta.xml file that describes what's in the zipped folder.

> ## Exercise
> 
> Challenge: Download this [Darwin Core Archive](https://www1.usgs.gov/obis-usa/ipt/archive.do?r=tpwd_harc_texasaransasbay_bagseine&v=2.3) and examine what's in it. Did you find anything unusual or that you don't understand what it is?
> 
> > ## Solution
> > ```bash
> > tree dwca-ambon_zooplankton_2017-v1.2/
> > ```
> > ```output
> >  dwca-ambon_zooplankton_2017-v1.2/
> >  |-- eml.xml
> >  |-- event.txt
> >  |-- extendedmeasurementorfact.txt
> >  |-- meta.xml
> >  |-- occurrence.txt
> > ```
> {: .solution}
{: .challenge}

### Darwin Core Mapping
Now that we understand a bit more about why Darwin Core was created and how it's used today we can begin the work of mapping data to the standard. The key resource when mapping data to Darwin Core is the [Darwin Core Quick Reference Guide](https://dwc.tdwg.org/terms/). This document provides an easy-to-read reference of the currently recommended terms for the Darwin Core standard. There are a lot of terms there and you won't use them all for every dataset (or even use them all on any dataset). As your experience grows with mapping to these terms you might gain experience with each term 😊 While it is not a requirement to have your column headers match the Darwin Core terms, as there are mechanisms to do the mapping, we highly recommend changing the column names to match the Darwin Core term verbatim. **Matt comment: My attempt at explaining that the column headers should be the Darwin Core terms verbatim. While hinting at how the meta.xml file can be used to do the mapping.**

> ## Exercise
> 
> **Challenge:** Find the matching Darwin Core term for these column headers.
> 
> 1. SAMPLE_DATE (example data: 09-MAR-21 05.45.00.000000000 PM)
> 2. lat (example data: 32.6560)
> 3. depth_m (example data: 6)
> 4. COMMON_NAME (example data: staghorn coral)
> 5. percent_cover (example data: 15)
> 6. COUNT (example data: 2 Females)
> 
> > ## Solution
> > 1. [`eventDate`](https://dwc.tdwg.org/terms/#dwc:eventDate)
> > 2. [`decimalLatitude`](https://dwc.tdwg.org/terms/#dwc:decimalLatitude)
> > 3. [`minimumDepthInMeters`](https://dwc.tdwg.org/terms/#dwc:minimumDepthInMeters) and [`maximumDepthInMeters`](https://dwc.tdwg.org/terms/#dwc:maximumDepthInMeters)
> > 4. [`vernacularName`](https://dwc.tdwg.org/terms/#dwc:vernacularName)
> > 5. [`organismQuantity`](https://dwc.tdwg.org/terms/#dwc:organismQuantity) and [`organismQuantityType`](https://dwc.tdwg.org/terms/#dwc:organismQuantityType)
> > 6. This one is tricky- it's two terms combined and will need to be split. [`indvidualCount`](https://dwc.tdwg.org/terms/#dwc:individualCount) and [`sex`](https://dwc.tdwg.org/terms/#dwc:sex)
> >
> > {: .output}
> {: .solution}
{: .challenge}

> ## Tip 
> To make the mapping step easier on yourself, we recommend starting a mapping document/spreadsheet (or document it as a comment in your script). List out all of your column headers in one column and document the appropriate Dawin Core term(s) in a second column. For example:
> 
> | my term | DwC term |
> |---------|----------|
> | lat | decimalLatitude |
> | date | eventDate |
> | species | scientificName |
{: .callout}


### What are the **required** Darwin Core terms for publishing to OBIS?
When doing your mapping some required information may be missing. These are the Darwin Core terms that are required to share your data to OBIS plus a few that are needed for GBIF.

| Darwin Core Term | Definition | Comment | Example |
|------------------|------------------------------------|---------------------------------------|-----------------|
| [`occurrenceID`](https://dwc.tdwg.org/terms/#dwc:occurrenceID) | An identifier for the Occurrence (as opposed to a particular digital record of the occurrence). In the absence of a persistent global unique identifier, construct one from a combination of identifiers in the record that will most closely make the occurrenceID globally unique. | To construct a globally unique identifier for each occurrence you can usually concatenate station + date + scientific name (or something similar) but you'll need to check this is unique for each row in your data. | `Station_95_Date_09JAN1997:14:35:00.000_Atractosteus_spatula` |
| [`basisOfRecord`](https://dwc.tdwg.org/terms/#dwc:basisOfRecord) | The specific nature of the data record.  | Pick from these controlled vocabulary terms: [HumanObservation](http://rs.tdwg.org/dwc/terms/HumanObservation), [MachineObservation](http://rs.tdwg.org/dwc/terms/MachineObservation), [PreservedSpecimen](http://rs.tdwg.org/dwc/terms/PreservedSpecimen), [LivingSpecimen](http://rs.tdwg.org/dwc/terms/LivingSpecimen), [FossilSpecimen](http://rs.tdwg.org/dwc/terms/FossilSpecimen) | `HumanObservation` |
| [`scientificName`](https://dwc.tdwg.org/terms/#dwc:scientificName) | The full scientific name, with authorship and date information if known. When forming part of an Identification, this should be the name in lowest level taxonomic rank that can be determined. This term should not contain identification qualifications, which should instead be supplied in the `identificationQualifier` term. | Note that cf., aff., etc. need to be parsed out to the `identificationQualifier` term. | `Atractosteus spatula` |
| [`scientificNameID`](https://dwc.tdwg.org/terms/#dwc:scientificNameID) | An identifier for the nomenclatural (not taxonomic) details of a scientific name. | Must be a WoRMS LSID for sharing to OBIS. Note that the numbers at the end are the AphiaID from WoRMS. | `urn:lsid:marinespecies.org:taxname:218214` |
| [`eventDate`](https://dwc.tdwg.org/terms/#dwc:eventDate) | The date-time or interval during which an Event occurred. For occurrences, this is the date-time when the event was recorded. Not suitable for a time in a geological context. | Must follow [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). See more information on dates in the [Data Cleaning]({{ page.root }}/03-data-cleaning/index.html) section of the workshop. | `2009-02-20T08:40Z` |
| [`decimalLatitude`](https://dwc.tdwg.org/terms/#dwc:decimalLatitude) | The geographic latitude (in decimal degrees, using the spatial reference system given in geodeticDatum) of the geographic center of a Location. Positive values are north of the Equator, negative values are south of it. Legal values lie between -90 and 90, inclusive. | For OBIS and GBIF the required `geodeticDatum` is WGS84. Uncertainty around the geographic center of a Location (e.g. when sampling event was a transect) can be recorded in `coordinateUncertaintyInMeters`. See more information on coordinates in the [Data Cleaning]({{ page.root }}/03-data-cleaning/index.html) section of the workshop. | `-41.0983423` |
| [`decimalLongitude`](https://dwc.tdwg.org/terms/#dwc:decimalLongitude) | The geographic longitude (in decimal degrees, using the spatial reference system given in geodeticDatum) of the geographic center of a Location. Positive values are east of the Greenwich Meridian, negative values are west of it. Legal values lie between -180 and 180, inclusive | For OBIS and GBIF the required `geodeticDatum` is WGS84. See more information on coordinates in the [Data Cleaning]({{ page.root }}/03-data-cleaning/index.html) section of the workshop. | `-121.1761111` |
| [`occurrenceStatus`](https://dwc.tdwg.org/terms/#dwc:occurrenceStatus) | For occurrences, the default vocabulary is recommended to consist of `present` and `absent`, but can be extended by implementers with good justification. | For OBIS, only valid values are `present` and `absent`. | `present` |
| [`countryCode`](https://dwc.tdwg.org/terms/#dwc:countryCode) | The standard code for the country in which the location occurs. | Use an [ISO 3166-1-alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. Not required for OBIS but GBIF needs this for their system. | `US` |
| [`kingdom`](https://dwc.tdwg.org/terms/#dwc:kingdom) | The full scientific name of the kingdom in which the taxon is classified.| Not required for OBIS but GBIF needs this to disambiguate scientific names that are the same but in different kingdoms. | `Animalia` |
| [`geodeticDatum`](https://dwc.tdwg.org/terms/#dwciri:geodeticDatum) | The ellipsoid, geodetic datum, or spatial reference system (SRS) upon which the geographic coordinates given in decimalLatitude and decimalLongitude as based. | Must be [WGS84](https://epsg.io/4326) for data shared to OBIS and GBIF but it's best to state explicitly that it is. | `WGS84` |

### What other terms should be considered?
While these terms are not required for publishing data to OBIS, they are extremely helpful for downstream users because without them the data are less useful for future analyses. For instance, `depth` is a crucial piece of information for marine observations, but it is not always included. For the most part the ones listed below are not going to be sitting there in the data, so you'll have to determine what the values should be and add them in. Really try your hardest to include them if you can.

| Darwin Core Term | Definition | Comment | Example |
|------------------|------------------------------------|---------------------------------------|--| 
| [`minimumDepthInMeters`](https://dwc.tdwg.org/terms/#dwc:minimumDepthInMeters) | The lesser depth of a range of depth below the local surface, in meters. | There isn't a single depth value (although there is `verbatimDepth` so even if you have a single value you'll put that in both minimum and maximum depth fields. | `0.1` |
| [`maximumDepthInMeters`](https://dwc.tdwg.org/terms/#dwc:maximumDepthInMeters) | 	The greater depth of a range of depth below the local surface, in meters. | For observations above sea level consider using [`maximumElevationInMeters`](https://dwc.tdwg.org/terms/#dwc:maximumElevationInMeters) and [`minimumElevationInMeters`](https://dwc.tdwg.org/terms/#dwc:minimumElevationInMeters) | `10.5` |
| [`coordinateUncertaintyInMeters`](https://dwc.tdwg.org/terms/#dwc:coordinateUncertaintyInMeters) | 	The horizontal distance (in meters) from the given decimalLatitude and decimalLongitude describing the smallest circle containing the whole of the Location. Leave the value empty if the uncertainty is unknown, cannot be estimated, or is not applicable (because there are no coordinates). Zero is not a valid value for this term | There's always uncertainty associated with locations. Recording the uncertainty is crucial for downstream analyses. | `0.1` |
| [`samplingProtocol`](https://dwc.tdwg.org/terms/#dwc:samplingProtocol) | The names of, references to, or descriptions of the methods or protocols used during an Event. |  | `Bag Seine` |
| [`taxonRank`](https://dwc.tdwg.org/terms/#dwc:taxonRank) | The taxonomic rank of the most specific name in the scientificName. | Also helps with disambiguation of scientific names. | `Species` |
| [`organismQuantity`](https://dwc.tdwg.org/terms/#dwc:organismQuantity) | A number or enumeration value for the quantity of organisms. | OBIS also likes to see this in the Extended Measurement or Fact extension. | `2` |
| [`organismQuantityType`](https://dwc.tdwg.org/terms/#dwc:organismQuantityType) | The type of quantification system used for the quantity of organisms. |  | `Relative Abundance` |
| [`datasetName`](https://dwc.tdwg.org/terms/#dwc:datasetName) | 	The name identifying the data set from which the record was derived. |  | `TPWD HARC Texas Coastal Fisheries Aransas Bag Bay Seine` |
| [`dataGeneralizations`](https://dwc.tdwg.org/terms/#dwc:dataGeneralizations) | 	Actions taken to make the shared data less specific or complete than in its original form. Suggests that alternative data of higher quality may be available on request. | This veers somewhat into the realm of metadata and will not be applicable to all datasets but if the data were modified such as due to sensitive species then it's important to note that for future users. | Coordinates generalized from original GPS coordinates to the nearest half degree grid cell |
| [`informationWithheld`](https://dwc.tdwg.org/terms/#dwc:informationWithheld) | 	Additional information that exists, but that has not been shared in the given record. | Also useful if the data have been modified this way for sensitive species or for other reasons. | `location information not given for endangered species` |
| [`institutionCode`](https://dwc.tdwg.org/terms/#dwc:institutionCode) | 	The name (or acronym) in use by the institution having custody of the object(s) or information referred to in the record. |  | `TPWD` |

Other than these specific terms, work through the data that you have and try to crosswalk it to the Darwin Core terms that match best. 

> ## Exercise
> 
> Challenge: Create some crosswalk notes for your dataset.
> 
> Compare your data files to the table(s) above to devise a plan to crosswalk your data columns into the DwC terms. 
> Use [this google form](https://docs.google.com/forms/d/e/1FAIpQLScOUKLA5t-hxWlPUBe1hJQXxwsd1hb94x-fopC9m2fot8h0pA/viewform?usp=sf_link) to submit your notes.
> 
{: .challenge}

{% include links.md %}

