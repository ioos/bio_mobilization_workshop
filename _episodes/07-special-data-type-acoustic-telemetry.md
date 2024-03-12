---
title: "Specific Data Examples - Acoustic Telemetry"
teaching: 15
exercises: 0
questions:
- "How does acoustic telemetry data convert to Darwin Core?"
- "How do I contribute my acoustic telemetry data to OBIS?"
objectives:
- "Collaborating with a network"
- "Understanding the mappings and what metadata and data are important to converting acoustic telemetry to Darwin Core"
- "Contributing tracking data for animals that are monitored with multiple methods of electronic or mark-recapture tracking regimes. (Acoustic, Satellite, RFID, coded-wire)"
keypoints:
- "The Ocean Tracking Network is the thematic OBIS node for animal telemetry data."
- "Mature pipelines exist to take acoustic telemetry data from projects contributing to OTN or to its regional nodes and publish standard, summarized datasets to OBIS." 
---

# Acoustic Telemetry Data
### How It Works

 Acoustic telemetry is a general term that describes the practice of implanting marine animals with electronic tags that emit an identifiable coded set of 'pings' to transmit a unique identifier to any listening station that is near enough to record them. Many companies sell systems of coded transmitters (tags) and listening devices (receivers) to allow researchers to track the movements of underwater animals at sub-1km scales. Recent developments allow for many listening stations to synchronize their detection of a 'ping' to allow for fine-scale triangulation of animal position.

 

### Networks - getting more data for your tracked animals

 Acoustic telemetry equipment is often intercompatible, allowing the listening stations of one project to detect the tagged individuals from any number of other projects. To maximize the utility of their tag detection data and the detectability of their tagged animals, many researchers engaged in acoustic telemetry research contribute their data to a data aggregating network. The global-scale aggregation network for handling and cross-referencingthis data is the Ocean Tracking Network, who coordinate many regional networks towards intercompatibility and harmonize the quality control and data pipelines to ensure all networks are able to contribute to a global observation network. Today that network-of-networks has many thousands of listening stations and tracks tens of thousands of active acoustic tags globally. Details on what the Ocean Tracking Network and its partners are currently observing are available at https://members.oceantrack.org/statistics/

### Preparing to publish to OBIS - how we solve the many-fish vs. one-fish-many-times problem

 Each of the telemetry networks produce for their investigators a data report that takes into account every compatible listening device across all of the networks that has heard their tagged animals. These reports can run into the millions of detections for anadromous fish, closed system monitoring, or where an animal may be resident near a listening device (or deceased near one). The Ocean Tracking Network has created a data pipeline for projects that combine all the observations for a certain project into a DarwinCore Event Core archive.
 
 When preparing to submit this data to the Ocean Biodiversity Information System, we as data managers must consider how to put these tens or hundreds of thousands of animal locations into the context of the broader database. By making summaries of the animal position data, and by using the organismID field to denote multiple positions for a single known individual organism, the OTN publication process allows telemetry data to contribute fully to the OBIS database without creating too much data density or losing the details of each individual animal's movement history.
 

### Mapping example

OTN maintains this wiki entry example of how to populate each of the Darwin Core fields for an acoustic telemetry-sourced data Darwin Core archive.

https://github.com/tdwg/dwc-for-biologging/wiki/Acoustic-sensor-enabled-tracking-of-blue-sharks 

### Satellite telemetry, light-level geolocation, etc.

 Satellite telemetry presumes surfacing events to obtain a GPS or Argos network location for a tagged individual. These 


### Multiple-method tagging of animals

Often, animals are tagged with multiple technologies to better capture their movement over smaller and larger distances.


{% include links.md %}
