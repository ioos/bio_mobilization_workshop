---
title: "Introduction to Darwin Core"
start: true
teaching: 0
exercises: 90
questions:
- "What is Darwin Core?"
- "What is a Darwin Core Archive?"
- "What is a core and what is an extension in Darwin Core?"
- "Why do people use Darwin Core for their data?"
- "What is OBIS-ENV-DATA aka (Event with Extended Measurement or Fact)?"
- "What are the required Darwin Core terms for sharing to OBIS?"
objectives:
- "Understand the purpose of Darwin Core."
- "Understand how to map data to Darwin Core."
- "Interact with GitHub and biological data."
- "Get data loaded into program of choice."
- "Plan for mapping to Darwin Core."
keypoints:
- "Darwin Core isn't difficult to apply, it just takes a little bit of time."
- "Using Darwin Core allows datasets from across projects, organizations, and countries to be integrated together."
- "Applying certain general principles to the data will make it easier to map to Darwin Core."
- "Implementing Darwin Core makes data FAIR-er and means becoming part of a community of people working together to understand species no matter where they work or are based."
---
# Darwin Core - A global community of data sharing and integration
Darwin Core is a data standard that was originally created to mobilize and share natural history collection data but has expanded to allow of exchange and sharing of many types of biological data including citizen scientist data, ecological monitoring data, eDNA data, telemetry data, taxonomic treatments, and many other types of biological data. Darwin Core is applicable to any data that observes an organism (scientific name, OTU, or other methods of defining a species) at a particular place and time. In Darwin Core this is an `occurrence`. To learn more about the foundations of Darwin Core read [Wieczorek et al. 2012](https://doi.org/10.1371/journal.pone.0029715).

### Demonstrated Use of Darwin Core
The power of Darwin Core is most evident in the data aggregators that harvest data using that standard. The one we will refer to most frequently in this workshop is the [Ocean Biodiversity Information System](https://obis.org/) (learn more about [OBIS](https://youtu.be/E6NblAC-1uE)). Another prominent one is the [Global Biodiversity Information Facility](https://www.gbif.org/) (learn more about [GBIF](https://vimeo.com/434831655)). It's also used by the Atlas of Living Australia, iDigBio among others. 

### Darwin Core Archives
Darwin Core Archives are what OBIS and GBIF are expecting to harvest into their systems. Fortunately the software created and maintained by GBIF, the [Integrated Publishing Toolkit](https://www.gbif.org/ipt) produces Darwin Core Archives for us. But Darwin Core Archives are pretty simple. It's a zipped folder containing the data (one or several files depending on how many extensions you use), an EML metadata XML file, and a meta.xml file that describes what's in the zipped folder.

> ## Exercise
> 
> Download this [Darwin Core Archive](https://www1.usgs.gov/obis-usa/ipt/archive.do?r=tpwd_harc_texasaransasbay_bagseine&v=2.3) and examine what's in it. Did you find anything unusual or that you don't understand what it is?
> > {: .output}

### Darwin Core Mapping
Now that we understand a bit more about why Darwin Core was created and how it's used today we can begin the work of mapping data to the standard. The key place you need when mapping data to Darwin Core is the [Darwin Core Quick Reference Guide](https://dwc.tdwg.org/terms/). But there are a lot of terms there and you won't use them all for every dataset (or even use them all on any dataset). You might use all the terms once you've mapped many datasets though 😊

> ## Exercise
> 
> Challenge: Find the matching Darwin Core term for these column headers.
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

### What are the Required Darwin Core terms for Publishing to OBIS?
When doing your mapping some required information may be missing. These are the Darwin Core terms that are required to share your data to OBIS plus a few that are needed for GBIF.

| Darwin Core Term | Definition | Comment |
|------------------|------------------------------------|---------------------------------------|
| [`occurrenceID`](https://dwc.tdwg.org/terms/#dwc:occurrenceID) | An identifier for the Occurrence (as opposed to a particular digital record of the occurrence). In the absence of a persistent global unique identifier, construct one from a combination of identifiers in the record that will most closely make the occurrenceID globally unique. | To construct a globally unique identifier for each occurrence you can usually concatenate station + date + scientific name (or something similar) but you'll need to check this is unique for each row in your data |
| [`basisOfRecord`](https://dwc.tdwg.org/terms/#dwc:basisOfRecord) | The specific nature of the data record.  | Controlled vocabulary: HumanObservation, MachineObservation, PreservedSpecimen, LivingSpecimen, FossilSpecimen|
| [`scientificName`](https://dwc.tdwg.org/terms/#dwc:scientificName) | The full scientific name, with authorship and date information if known. When forming part of an Identification, this should be the name in lowest level taxonomic rank that can be determined. This term should not contain identification qualifications, which should instead be supplied in the IdentificationQualifier term. | Note that cf., aff., etc. need to be parsed out to the `identificationQualifier` term |
| [`scientificNameID`](https://dwc.tdwg.org/terms/#dwc:scientificNameID) | An identifier for the nomenclatural (not taxonomic) details of a scientific name. | Must be a WoRMS LSID for sharing to OBIS. Example: urn:lsid:marinespecies.org:taxname:218214. Note that the numbers at the end are the AphiaID from WoRMS. |
| [`eventDate`](https://dwc.tdwg.org/terms/#dwc:eventDate) | The date-time or interval during which an Event occurred. For occurrences, this is the date-time when the event was recorded. Not suitable for a time in a geological context. | Must follow [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) |
| [`decimalLatitude`](https://dwc.tdwg.org/terms/#dwc:decimalLatitude) | The geographic latitude (in decimal degrees, using the spatial reference system given in geodeticDatum) of the geographic center of a Location. Positive values are north of the Equator, negative values are south of it. Legal values lie between -90 and 90, inclusive. | For OBIS and GBIF the required `geodeticDatum` is WGS84. |
| [`decimalLongitude`](https://dwc.tdwg.org/terms/#dwc:decimalLongitude) | The geographic longitude (in decimal degrees, using the spatial reference system given in geodeticDatum) of the geographic center of a Location. Positive values are east of the Greenwich Meridian, negative values are west of it. Legal values lie between -180 and 180, inclusive | For OBIS and GBIF the required `geodeticDatum` is WGS84. |
| [`occurrenceStatus`](https://dwc.tdwg.org/terms/#dwc:occurrenceStatus) | For Occurrences, the default vocabulary is recommended to consist of "present" and "absent", but can be extended by implementers with good justification. | For OBIS, only valid values are "present" and "absent". |
| [`countryCode`](https://dwc.tdwg.org/terms/#dwc:countryCode) | The standard code for the country in which the Location occurs. | 	Use an [ISO 3166](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes)-1-alpha-2 country code. Not required for OBIS but GBIF needs this for their system.|
| [`kingdom`](https://dwc.tdwg.org/terms/#dwc:kingdom) | The full scientific name of the kingdom in which the taxon is classified. | Not required for OBIS but GBIF needs this to disambiguate scientific names that are the same in different kingdoms. |
| [`geodeticDatum`](https://dwc.tdwg.org/terms/#dwciri:geodeticDatum) | The ellipsoid, geodetic datum, or spatial reference system (SRS) upon which the geographic coordinates given in decimalLatitude and decimalLongitude as based. | Must be WGS84 for data shared to OBIS and GBIF but it's best to state explicitly that it is. |

### What other terms should be considered?
While these terms are not required for publishing data to OBIS, they are extremely helpful for downstream users because without them the data are less useful for future analyses. For instance depth is a crucial piece of information for marine observations but it is not always included. For the most part the ones listed below are not going to be sitting there in the data so you'll have to determine what the values should be and add these in. Really try your hardest to include these ones if you can.

| Darwin Core Term | Definition | Comment |
|------------------|------------------------------------|---------------------------------------|
| [`minimumDepthInMeters`](https://dwc.tdwg.org/terms/#dwc:minimumDepthInMeters) | The lesser depth of a range of depth below the local surface, in meters. | There isn't a single depth value (although there is `verbatimDepth` so even if you have a single value you'll put that in both minimum and maximum depth fields. |
| [`maximumDepthInMeters`](https://dwc.tdwg.org/terms/#dwc:maximumDepthInMeters) | 	The greater depth of a range of depth below the local surface, in meters. |  |
| [`coordinateUncertaintyInMeters`](https://dwc.tdwg.org/terms/#dwc:coordinateUncertaintyInMeters) | 	The horizontal distance (in meters) from the given decimalLatitude and decimalLongitude describing the smallest circle containing the whole of the Location. Leave the value empty if the uncertainty is unknown, cannot be estimated, or is not applicable (because there are no coordinates). Zero is not a valid value for this term | There's always uncertainty associated with locations. Recording the uncertainty is crucial for downstream analyses. |
| [`samplingProtocol`](https://dwc.tdwg.org/terms/#dwc:samplingProtocol) | The names of, references to, or descriptions of the methods or protocols used during an Event. |  |
| [`taxonRank`](https://dwc.tdwg.org/terms/#dwc:taxonRank) | The taxonomic rank of the most specific name in the scientificName. | Also helps with disambiguation of scientific names. |
| [`organismQuantity`](https://dwc.tdwg.org/terms/#dwc:organismQuantity) | A number or enumeration value for the quantity of organisms. | OBIS also likes to see this in the Extended Measurement or Fact extension. |
| [`organismQuantityType`](https://dwc.tdwg.org/terms/#dwc:organismQuantityType) | The type of quantification system used for the quantity of organisms. |  |
| [`datasetName`](https://dwc.tdwg.org/terms/#dwc:datasetName) | 	The name identifying the data set from which the record was derived. |  |
| [`dataGeneralizations`](https://dwc.tdwg.org/terms/#dwc:dataGeneralizations) | 	Actions taken to make the shared data less specific or complete than in its original form. Suggests that alternative data of higher quality may be available on request. | This veers somewhat into the realm of metadata and will not be applicable to all datasets but if the data were modified such as due to sensitive species then it's important to note that for future users. |
| [`informationWithheld`](https://dwc.tdwg.org/terms/#dwc:informationWithheld) | 	Additional information that exists, but that has not been shared in the given record. | Also useful if the data have been modified this way for sensitive species or for other reasons. |
| [`institutionCode`](https://dwc.tdwg.org/terms/#dwc:institutionCode) | 	The name (or acronym) in use by the institution having custody of the object(s) or information referred to in the record. |  |

Other than these just take the data that you have and crosswalk it to the Darwin Core terms that match best. 

### Darwin Core - Cores and Extensions
Now that we have a firm basis for understanding the different terms in Darwin Core the next part to understand is the difference between cores and extensions. You will always have a core (occurrence core or event core) with no extensions or several. What you choose depends on the data you have and how to represent it best. The original Darwin Core core is the [occurrence core](https://tools.gbif.org/dwca-validator/extension.do?id=dwc:occurrence). Once people started using that core they began to see that they needed extensions to that core to best represent the data they were trying to share and therefore [several extensions](https://tools.gbif.org/dwca-validator/extensions.do) have been developed (and are continuing to be developed). Over time as more monitoring data has been shared there was another core type added called [event core](https://tools.gbif.org/dwca-validator/extension.do?id=dwc:event). Without getting too far into the weeds on the cores and extensions what's most important to understand is that you need to pick your core type and once you do that then you pick the extensions to go with it. If your data took place as part of an event (cruise, transects, etc) you'll pick event core.

An innovation that OBIS made in this space was introducing the Extended Measurement or Fact extension (also sometimes referred to as OBIS-ENV-DATA). This uses the event core with an occurrence extension + the [extended measurement or fact extension](https://tools.gbif.org/dwca-validator/extension.do?id=http://rs.iobis.org/obis/terms/ExtendedMeasurementOrFact). This extension makes it possible to include measurements for both the events (salinity, temperature, dissolved oxygen, gear type, etc) as well as measurements about the occurrences (weight, length, etc). Prior to this you were only able to include measurements of the occurrence. 

Over at the IOOS Bio Data Guide Github you can see [a script](https://github.com/ioos/bio_data_guide/blob/main/datasets/TPWD_HARC_BagSeine/TPWD_HARC_BagSeine_OBISENV.md) that was used to take data in it's original form and align it to Darwin Core Event Core with Extended Measurement or Fact.

1. Intro / background
   1. to DwC https://github.com/OBISCanada/obis-workshop/blob/master/README.md 
   2. To OBIS https://www.youtube.com/channel/UCokyj9fP5DMQfIdUhtZT9tw/featured 
2. How to interact with the SMBD, Github
3. Get data loaded into R or Python
4. Planning for mapping into DwC
   1. What DwC terms are included in your dataset: exercise
   2. Searching in NERC



{% include links.md %}

