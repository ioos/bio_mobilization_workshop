---
title: "Acoustic (and Satellite) Telemetry"
teaching: 15
exercises: 0
---

:::::::::::: questions

- How does acoustic telemetry data convert to Darwin Core?
- How do I contribute my acoustic telemetry data to OBIS?

::::::::::::::::::::::

::::::::::: objectives

- Collaborating with a network
- Understanding the mappings and what metadata and data are important to converting acoustic telemetry to Darwin Core
- Contributing tracking data for animals that are monitored with multiple methods of electronic or mark-recapture 
tracking regimes. (Acoustic, Satellite, RFID, coded-wire)

::::::::::::::::::::::

## Acoustic and Satellite Telemetry Data

### Acoustic Telemetry

#### How It Works

Acoustic telemetry is a general term that describes the practice of implanting marine animals with electronic tags that 
emit an identifiable coded set of 'pings' to transmit a unique identifier to any listening station that is near enough 
to record them. Many companies sell systems of coded transmitters (tags) and listening devices (receivers) to allow 
researchers to track the movements of underwater animals at sub-1km scales. Recent developments allow for many 
listening stations to synchronize their detection of a 'ping' to allow for fine-scale triangulation of animal position.

#### Networks - getting more data for your tracked animals

Acoustic telemetry equipment is often intercompatible, allowing the listening stations of one project to detect the 
tagged individuals from any number of other projects. To maximize the utility of their tag detection data and the 
detectability of their tagged animals, many researchers engaged in acoustic telemetry research contribute their data 
to a data aggregating network. The global-scale aggregation network for handling and cross-referencing this data is 
the Ocean Tracking Network, who coordinate many regional networks towards intercompatibility and harmonize the quality 
control and data pipelines to ensure all networks are able to contribute to a global observation network. Today that 
network-of-networks has many thousands of listening stations and tracks tens of thousands of active acoustic tags 
globally. Details on what the Ocean Tracking Network and its partners are currently observing are available at 
https://members.oceantrack.org/statistics/

![screenshot](../episodes/fig/acoustic_telemetry_components.png)

#### Preparing to publish to OBIS - how we solve the many-fish vs. one-fish-many-times problem

Each of the telemetry networks produce for their investigators a data report that takes into account every compatible 
listening device across all of the networks that has heard their tagged animals. This report is intended to be the best, 
most complete report available for all possible detections of the studied animals from all participating partners 
worldwide. These reports can run into the millions of detections for anadromous fish, closed system monitoring, or 
where an animal may be resident near a listening device (or deceased near one). The Ocean Tracking Network has created 
a data pipeline for projects that combine all the observations for a certain project into a Darwin Core Event Core 
archive, based on a shared standard built between the European Tracking Network and the Ocean Tracking Network that can 
produce an Occurrence Core or Event Core dataset.

When preparing to submit animal telemetry data to the Ocean Biodiversity Information System, we as data managers must 
consider how to put these tens or hundreds of thousands of individual animal locations into the context of the broader 
database. By making time-binned summaries of the animal position data, and by using the organismID field to denote 
multiple positions for a single known individual organism, the OTN publication process allows telemetry data to 
contribute fully to the OBIS database without creating too much data density or losing the details of each individual 
animal's movement history.

Below is a small table highlighting how one might make a time-binned summary of observations. In this example, we 
truncate the date-times down to the day+hour, then see if there are duplicate values. If so, we keep the first value 
but drop the other values that fall in that same hour.

::::::::::::::::: spoiler

### Time binning example

| time                 | dayhr         | Keep?   |
|:---------------------|:--------------|:--------|
| 2009-09-23T00:00:00Z | 2009-09-23T00 | True    |
| 2009-09-25T06:42:00Z | 2009-09-25T06 | True    |
| 2009-09-25T11:09:00Z | 2009-09-25T11 | True    |
| 2009-09-25T11:11:00Z | 2009-09-25T11 | False   |
| 2009-09-25T11:30:00Z | 2009-09-25T11 | False   |
| 2009-09-27T17:58:00Z | 2009-09-27T17 | True    |
| 2009-09-30T05:01:00Z | 2009-09-30T05 | True    |
| 2009-10-08T20:24:00Z | 2009-10-08T20 | True    |
| 2009-10-15T11:05:00Z | 2009-10-15T11 | True    |
| 2009-10-17T06:11:00Z | 2009-10-17T06 | True    |
| 2009-10-17T09:00:00Z | 2009-10-17T09 | True    |
| 2009-10-17T10:38:00Z | 2009-10-17T10 | True    |
| 2009-10-18T08:48:00Z | 2009-10-18T08 | True    |
| 2009-10-18T10:26:00Z | 2009-10-18T10 | True    |
| 2009-10-18T11:15:00Z | 2009-10-18T11 | True    |
| 2009-10-19T10:20:00Z | 2009-10-19T10 | True    |
| 2009-10-23T23:52:00Z | 2009-10-23T23 | True    |
| 2009-10-24T00:06:00Z | 2009-10-24T00 | True    |
| 2009-10-26T10:53:00Z | 2009-10-26T10 | True    |
| 2009-10-26T11:22:00Z | 2009-10-26T11 | True    |
| 2009-10-27T16:21:00Z | 2009-10-27T16 | True    |
| 2009-10-27T16:22:00Z | 2009-10-27T16 | False   |
| 2009-10-27T16:42:00Z | 2009-10-27T16 | False   |
| 2009-10-29T11:53:00Z | 2009-10-29T11 | True    |
| 2009-10-30T10:03:00Z | 2009-10-30T10 | True    |
| 2009-10-31T19:48:00Z | 2009-10-31T19 | True    |
| 2009-10-31T21:15:00Z | 2009-10-31T21 | True    |
| 2009-11-01T21:04:00Z | 2009-11-01T21 | True    |
| 2009-11-06T17:53:00Z | 2009-11-06T17 | True    |
| 2009-11-13T18:48:00Z | 2009-11-13T18 | True    |
| 2009-11-23T05:12:00Z | 2009-11-23T05 | True    |

:::::::::::::::::::::::::

#### Mapping example

OTN maintains this wiki entry example of how to populate each of the Darwin Core fields for an acoustic 
telemetry-sourced data Darwin Core archive. 

<https://github.com/tdwg/dwc-for-biologging/wiki/Acoustic-sensor-enabled-tracking-of-blue-sharks>

The key features of this schema are:

##### Metadata:
* Projects are organized around tagging efforts with the related research question and efforts included in the 
* Abstract/Project Description/Sampling Methods fields of the EML.
* Participants are those registered as participating in the tagging project, plus all PIs from the 'participating' 
* projects that supplied additional detection events with the role Data Contributor.

##### Data:
* Event records with associated Occurrence Extension for animal capture (for tagging purposes).
* Event records for tag attachment.
* Event records for receiver deployment (only for 'participating' receivers, who have contributed detections to the archive).
* Event records with associated Occurrence Extension for post-filtering detection events at a receiver, one per hour/individual detected.
    * Current filtering is the time-based Pincock filtering
    * More robust filters are in development, and will include speed and distance filtering, as well as a 'current known home range' filter
* Optional eMoF records associated with capture Occurrences describing observed features of the tagged individuals like length, weight, sex, lifestage, etc.
* Optional eMoF records associated with receiver deployments describing any abiotic measurements being made by the receiver unit itself.
* Event records with parent Event records for any co-deployed instruments at a receiver deployment.
* Optional eMoF records associated with the instrument deployment.

Data provided to the Ocean Tracking Network or its Nodes (see <https://members.oceantrack.org> for the map of current 
Nodes ) can produce these packages automatically based on currently-reported data. The published datasets are available 
via OBIS, and OTN's OBIS Node at <https://members.oceantrack.org/ipt/>.


### Satellite telemetry, light-level geolocation, etc.

Satellite telemetry presumes surfacing events, to allow an instrument to obtain a GPS or Argos network location of a 
tagged individual. These surfacings are often monitored in near-realtime with a high degree of position error, and paths 
can be reprocessed and corrected post-deployment using light level geolocation, state-space modelling, or other emerging 
techniques. 

For satellite telemetry, tracks are not published automatically by OTN, but on a case-by-case basis. A method for 
publishing satellite-based animal telemetry data that conforms to the ETN/OTN standard above as an Occurrence Core 
archive is explained here: <https://github.com/tdwg/dwc-for-biologging/wiki/Movebank-GPS-data>. The R package `movepub` 
implements this method and its SQL algorithm is also browsable on GitHub for those adapting it to use outside of R. 
<https://github.com/inbo/movepub/blob/main/inst/sql/dwc_occurrence.sql>

In the case of working with the [IOOS Animal Telemetry Network](https://atn.ioos.us/) for satellite telemetry data, 
tracks will be automatically archived at NOAA's 
[National Centers for Environmental Information](https://www.ncei.noaa.gov/) and published to 
[OBIS-USA](https://obis.org/node/b7c47783-a020-4173-b390-7b57c4fa1426), as identified by the scientist in the 
registration system. The mapping between the [ATN's netCDF archival format](https://ioos.github.io/ioos-atn-data/) 
submitted to NCEI and the Darwin Core format is currently being discussed in this 
[issue](https://github.com/ioos/bio_data_guide/issues/145).


#### Multiple-method tagging of animals

Often, animals are tagged with multiple technologies to better capture their movement over smaller and larger distances. 
The ability to combine both methods into a single file with the same data density and features described above is a very 
helpful feature of the OTN publication system. Combining the workflows above and harmonizing the many methods of 
detecting animal position via the organismID field is how we produce a rational combined record of animal position 
through time, across many methods. Here, the Occurrence/Event detection pair retains and explains the 'how' an animal 
was detected at each point while preserving a complete history for the organism in the Occurrence records.

![screenshot](../episodes/fig/tagged_seal.png)

Sometimes, stranger setups like animals-as-listening-stations or animals collecting oceanographic data can be part of 
your project. This extends the default schema with some extra components, but nothing is impossible within Event Core!


#### Providing your telemetry data and metadata to an OTN node

If you want to publish animal telemetry data to OBIS and GBIF, OTN is a thematic OBIS node for animal telemetry and we 
are able to help you do that. Providing your data to OTN augments it with other potential detections that may have 
occurred outside your owned listening stations, quality controls the aggregated results, and produces the archive using 
the QCed metadata and data that you and your collaborators have provided to OTN. These archives are then automatically 
updated whenever new data or metadata are supplied that extends your project's dataset. It's the best way to guarantee 
there will be an accurate record of your study animals in OBIS now and into the future.

Supplying acoustic or satellite data to OTN or one of its Nodes can be done via our templates at 
<https://members.oceantrack.org/data/data-collection/>. Reporting the project metadata provides the information 
necessary to fulfill the EML metadata, and the Tag/Instrument metadata along with the detection files are the sources of 
the DwC archive's Event and Occurrence and eMoF data.

Telemetry for satellite tagged animals can be provided as-is, with an indication of whether it is raw or post-processed.

::::::::::::: keypoints

- The Ocean Tracking Network is the thematic OBIS node for animal telemetry data.
- Mature pipelines exist to take acoustic telemetry data from projects contributing to OTN or to its regional nodes and 
publish standard, summarized datasets to OBIS.

:::::::::::::::::::::::