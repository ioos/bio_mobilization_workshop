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

### The  of Darwin Core
The power of Darwin Core is most evident in the data aggregators that harvest data using that standard. The one we will refer to most frequently in this workshop is the [Ocean Biodiversity Information System](https://obis.org/) (learn more about [OBIS](https://youtu.be/E6NblAC-1uE)). Another prominent one is the [Global Biodiversity Information Facility](https://www.gbif.org/) (learn more about [GBIF](https://vimeo.com/434831655)). It's also used by the Atlas of Living Australia and iDigBio. 

### Darwin Core Archives
Darwin Core Archives are what OBIS and GBIF are expecting to harvest into their systems. Fortunately the software created and maintained by GBIF, the [Integrated Publishing Toolkit](https://www.gbif.org/ipt) produces Darwin Core Archives for us. But Darwin Core Archives are pretty simple. It's a zipped folder containing the data (one or several files depending on how many extensions you use), an EML metadata XML file, and a meta.xml file that describes what's in the zipped folder.

> ## Exercise
> 
> Download this [Darwin Core Archive](https://www1.usgs.gov/obis-usa/ipt/archive.do?r=tpwd_harc_texasaransasbay_bagseine&v=2.3) and examine what's in it. Did you find anything unusual or that you didn't understand what it is?

1. Intro / background
   1. to DwC https://github.com/OBISCanada/obis-workshop/blob/master/README.md 
   2. To OBIS https://www.youtube.com/channel/UCokyj9fP5DMQfIdUhtZT9tw/featured 
2. How to interact with the SMBD, Github
3. Get data loaded into R or Python
4. Planning for mapping into DwC
   1. What DwC terms are included in your dataset: exercise
   2. Searching in NERC



{% include links.md %}

