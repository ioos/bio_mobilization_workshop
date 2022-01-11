---
title: "Validating and publishing"
teaching: 0
exercises: 90
questions:
- "How can I validate and publish my data?"
objectives:
- "Compiling metadata for EML."
- "Data enhancement and quality control"
- "Validation of records."
keypoints:
- "Highlight required metadata fields in the Ecological Markup Language (EML)."
- "Discuss different packages (e.g. obistools, robis) that can be used to QA/QC data." 
- "Use the [GBIF data validator](https://www.gbif.org/tools/data-validator) to check your DwC archives & `.csv` files."
---

1. Creating EML metadata text file
2. Data enhancement and quality control
3. Validation of DwC archive files

# Ecological Markup Language (EML)

Both OBIS and GBIF have the Ecological Markup Language (EML) as metadata standard. When publishing your data through GBIF's Integrated Publisher Toolkit (IPT), this tool helps you create an EML, which is implemented as XML (eml.xml), which will be one of the files in the Darwin Core Archive (DwC-A). As such, if you publish your own data through the IPT, there is no need for innate knowledge on the EML format. To produce an EML extension however, there are a minimum required number of fields that would need to be filled out through the IPT, these are: title, abstract, citation, and contact. 

_to do: create table like in 01-introduction_

Additional metadata terms to be considered adding (_include these in table above?_). If you are not publishing data yourself, it is important to provide the relevant information for someone else to fill out the IPT on your behalf, or for the extension to be included in the DwC-A .zip file. There are R packages that can help in developing an EML.xml file that includes all the relevant information. These packages are e.g. [EML](https://github.com/ropensci/EML), [emld](https://github.com/ropensci/emld) or [EMLassemblyline](https://ediorg.github.io/EMLassemblyline/articles/overview.html). 

# Data enhancement and quality control

OBIS performs a number of quality checks on the data it receives. Red quality flags are attached to occurrence records if errors are encountered, and records may also be rejected if they do not meet minimum requirements. The checks that OBIS performs are documented [here](https://github.com/iobis/obis-qc). Therefore, prior to publishing your data to OBIS and/or GBIF, it is important to perform quality control on your standardized data. This can help identify any outliers or "faulty" data. It will also help with ensuring that your data is compatible and interoperable with other datasets published to OBIS. There are numerous functions within the [robis](https://www.rdocumentation.org/packages/robis/versions/2.3.9) or [obistools](https://github.com/iobis/obistools) R packages that can serve to identify outliers, inspect quality or ensure that the dataset structure fits the required format for both the Event and Occurrence tables. 

> ## Exercise 
>
> Challenge #2: [download the following dataset] and the [robis] and [obistools] R packages. Then, perform the following minimal quality assurance and control checks: i) run a diagnostics report for the data quality, ii) ensure the data is in the correct structure, iii) plot the occurrences in a map, and iv) determine whether reported depths are accurate. _To do: create easy dataset to work with or link to dataset in JupyterNotebooks?_
> 
> > ## Solution
> > i. obistools::report(), or alternatively hmisc::describe()
> > ii. check_eventids() # checks if both eventID and parentEventID fields as present in the table, and whether all parentEventIDs have a corresponding eventID
> >     check_extension_eventids() # checks if eventIDs in an extension have matching eventIDs in the core table.
> >     flatten_event() and flatten_occurrence() # recursively adds event information from parent events to child events. 
> > iii. obistools::plot_map(), or robis::map_ggplot() # to plot occurrence records
> > iv. obistools::check_onland(), or check_depth()
> >  {: .output}
> {: .solution}
{: .challenge}

# Data validation

Once you've determined that there are no crazy outliers or flags raised with your dataset, and your dataset has been standardized to the DwC-A format, you can run the [GBIF Data Validator](https://www.gbif.org/tools/data-validator). By submitting a dataset to the validator tool, you can go through the validation and interpretation procedures and determine potential issues with the standardized data without having to publish it. The following files can be dropped or uploaded to the validator tool:

i. ZIP-compressed DwC-A (containing an Occurrence, Taxon or Event Core)
ii. IPT Excel templates containing Checklist, Occurrence, or Sampling-event data
iii. CSV files containing Darwin Core terms in the first _row_. 

The validation tool provides an indication of whether the dataset can be indexed by GBIF and OBIS or not, and provides a summary of issues found during interpretation of the dataset. The main advantage is that you don't have to publish your data through the IPT (and hence make it publicly visible) prior to determining any issues related to the data or metadata. You will be able to view the metadata as a draft version of the dataset page as it would appear when the dataset is published and registered with GBIF. It is typically the final step to be done prior to going through the IPT and publish your dataset. 

> ## Exercise : Try the GBIF DwC Validator
> 
> Challenge: Use the GBIF data validator to check a [DwC archive file] & document the issues with it.
> 
> _TODO: provide a sample DwC file to submit?_
>
>  > ## Solution
> > i. issue 1
> > 2. issue 2
> > {: .output}
> {: .solution}
{: .challenge}



{% include links.md %}