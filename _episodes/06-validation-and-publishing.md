---
title: "Metadata, validating, and publishing"
teaching: 0
exercises: 90
questions:
- "How can I validate and publish my data?"
objectives:
- "Compiling metadata for EML."
- "Data enhancement and quality control"
- "Validation of records."
keypoints:
- "Some metadata fields in the Ecological Markup Language (EML) are required for publishing to OBIS."
- "Several packages (e.g. obistools, robis, Hmisc) can be used to QA/QC data." 
- "Use the [GBIF data validator](https://www.gbif.org/tools/data-validator) to check your DwC archives & `.csv` files."
---

1. Creating EML metadata text file
2. Data enhancement and quality control
3. Validation of DwC archive files

# Integrated Publishing Toolkit
The [GBIF Integrated Publishing Toolkit (IPT)](https://www.gbif.org/ipt) is currently the only way to publish data to OBIS. [OBIS nodes](https://obis.org/contact/) host an IPT instance for their region or theme. The [OBIS-USA IPT](https://www1.usgs.gov/obis-usa/ipt/) (hosted at the USGS) is available for anyone in the US to publish their data to OBIS and GBIF. To publish using this IPT work with the OBIS-USA node manager, Abby Benson. You can choose to download and install your own instance of the IPT but it might be difficult to register it with OBIS. Instead it's recommended to work with one of the OBIS nodes to publish your data through their IPT. The requirements for publishing via an OBIS node IPT are that the data follows Darwin Core, includes the required Darwin Core and EML metadata elements, and you have contacted the node to ensure the data are a good fit for that node. 

![screenshot]({{ page.root }}/fig/DwC_workflow.jpg){: .image-with-shadow }


# Ecological Markup [Metadata?] Language (EML) 

Both OBIS and GBIF use [Ecological Markup [Metadata?] Language (EML)](https://eml.ecoinformatics.org/) as the metadata standard associated with the data. For the purposes of this workshop we will not dive into the world of EML. However, we should note that when publishing your data through the IPT, the IPT helps you create an EML file as part of the Darwin Core Archive (DwC-A). As such, if you publish your own data through the IPT, there is no need for innate knowledge on the EML format. But there are a minimum required number of fields that would need to be filled out in the IPT: `title`, `abstract`, `citation`, and several `contacts`.

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

* A note from Abby- I'm struggling with this section because most of it seems redundant to what's in the data. I'm not sure what other EML fields should really be considered. Maybe others have an opinion on this?
* Note from Tim - included Study Extent, Sampling Description and Step Description if data providers are keen to include more details on their research project. 

If you are interested in creating an EML metadata file, it is possible to upload those into the IPT. There are R packages that can help in developing an EML.xml file. These packages are e.g. [EML](https://github.com/ropensci/EML), [emld](https://github.com/ropensci/emld) or [EMLassemblyline](https://ediorg.github.io/EMLassemblyline/articles/overview.html). 

---
# Data enhancement and quality control

OBIS performs a number of quality checks on the data it receives. Red quality flags are attached to occurrence records if errors are encountered, and records may also be rejected if they do not meet minimum requirements. The checks that OBIS performs are documented [here](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4309024/pdf/bau125.pdf) and a python implementation is available [here](https://github.com/iobis/obis-qc). Therefore, prior to publishing your data to OBIS and/or GBIF, it is important to perform quality control on your standardized data. This can help identify any outliers or "faulty" data. It will also help with ensuring that your data is compatible and interoperable with other datasets published to OBIS. There are numerous functions within the [robis](https://www.rdocumentation.org/packages/robis/versions/2.3.9) or [obistools](https://github.com/iobis/obistools) R packages that can serve to identify outliers, inspect quality or 
ensure that the dataset structure fits the required format for both the Event and Occurrence tables. 

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
> **Challenge:** Install [obistools](https://github.com/iobis/obistools) and [Hmisc](https://cran.r-project.org/web/packages/Hmisc/Hmisc.pdf) R packages. Then, perform the following minimal quality assurance and control checks: i) run a diagnostics report for the data quality, ii) ensure the data is in the correct structure, iii) plot the occurrences in a map, and iv) determine whether reported depths are accurate. 
> 
> * Note from Tim: Do we want participants to do this with their own dataset? Or do we want to create an easy dataset to work with or link to dataset? [Enrique]: I suggest participants use a provided dataset with a few errors, e.g. occurrences on land or outside geographic range (wrong coordinates).
> 
> > ## Solution
> > ```
> > i. obistools::report(), and hmisc::describe()
> > ii. check_eventids() # checks if both eventID and parentEventID fields as present in the table, and whether all parentEventIDs have a corresponding eventID
> >     check_extension_eventids() # checks if eventIDs in an extension have matching eventIDs in the core table.
> >     flatten_event() and flatten_occurrence() # recursively adds event information from parent events to child events. 
> > iii. obistools::plot_map() # to plot occurrence records
> > iv. obistools::check_onland(), or check_depth()
> > ```
> >  {: .output}
> {: .solution}
{: .challenge}

# Data validation

Once you've determined that there are no crazy outliers or flags raised with your dataset, and your dataset has been standardized to the DwC-A format, you can run the [GBIF Data Validator](https://www.gbif.org/tools/data-validator). By submitting a dataset to the validator tool, you can go through the validation and interpretation procedures and determine potential issues with the standardized data without having to publish it. The following files can be dropped or uploaded to the validator tool:

i. ZIP-compressed DwC-A (containing an Occurrence, Taxon or Event Core)
ii. IPT Excel templates containing Checklist, Occurrence, or Sampling-event data
iii. CSV files containing Darwin Core terms in the first _row_. 

The validation tool provides an indication of whether the dataset can be indexed by GBIF and OBIS or not, and provides a summary of issues found during interpretation of the dataset. The main advantage is that you don't have to publish your data through the IPT (and hence make it publicly visible) prior to determining any issues related to the data or metadata. You will be able to view the metadata as a draft version of the dataset page as it would appear when the dataset is published and registered with GBIF. It is typically the final step to be done prior to going through the IPT and publish your dataset. 

> ## Example : Using the GBIF DwC Validator
> 
> The GBIF data validator can be used to check a DwC archive `.zip`. 
> The validator will highlight issues with the archive like bad rows, missing columns, and much more.
> 
> You can try using the validator with [this example DwC `.zip` file (hosted on gdrive)](https://drive.google.com/file/d/1iQ5TJg-GvZIhv-gdNrmx1ieTBZdEJE8a/view?usp=sharing) and see the issues with it.
>
>  > ## Solution
> > The following are issues with the provided DwC archive reported by the GBIF validator (as of 2022-01):
> > 1. Country derived from coordinates
> > 2. Taxon match fuzzy
> > 3. Taxon match higherrank
> > 4. Taxon match none
> > 5. Basis of record invalid
> > 6. Coordinate rounded
> > 7. Geodetic datum assumed WGS84
> > {: .output}
> {: .solution}
{: .challenge}

If you are at this stage with your own DwC-standardized dataset, run the GBIF validation tool to determine if there are any issues with your dataset!

{% include links.md %}
