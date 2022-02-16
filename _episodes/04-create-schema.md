---
title: "Creating schema"
start: true
teaching: 0
exercises: 120
questions:
- "What is a core and what is an extension in Darwin Core?"
- "What is OBIS-ENV-DATA aka (Event Core with Extended Measurement or Fact)?"
- "How do I create Darwin Core files?"
objectives:
- "Creating IDs."
- "Creating event file, occurrence file, eMOF file."
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"
---
### Darwin Core - Cores and Extensions
Now that we have a firm basis for understanding the different terms in Darwin Core the next part to understand is the difference between cores and extensions. You will always have a core (occurrence core or event core) with no extensions or several. What you choose depends on the data you have and how to represent it best. The original Darwin Core core is the [occurrence core](https://tools.gbif.org/dwca-validator/extension.do?id=dwc:occurrence). Once people started using that core they began to see that they needed extensions to that core to best represent the data they were trying to share and therefore [several extensions](https://tools.gbif.org/dwca-validator/extensions.do) have been developed (and are continuing to be developed). Over time as more monitoring data has been shared there was another core type added called [event core](https://tools.gbif.org/dwca-validator/extension.do?id=dwc:event). Without getting too far into the weeds on the cores and extensions what's most important to understand is that you need to pick your core type and once you do that then you pick the extensions to go with it. If your data took place as part of an event (cruise, transects, etc) you'll pick event core.

### Different options for sharing the data
#### Occurrence only
The bare minimum for sharing data to OBIS is to use the [Occurrence Core](https://tools.gbif.org/dwca-validator/extension.do?id=dwc:Occurrence) with no extensions. The occurrence core allows for providing all the required Darwin Core terms detailed in the [intro section](https://ioos.github.io/bio_mobilization_workshop/01-introduction/index.html). You can produce a fully compliant Darwin Core version of the data using only the occurrence core. However, if the data were collected using some kind of sampling methodology you will lose much of that information if you use this most simple form of the data. However, it is faster and easier to produce.

#### Occurrence Core + extensions
Using the occurrence core plus [relevant extensions](https://tools.gbif.org/dwca-validator/extensions.do) means that you can capture more of the data that's been recorded. 

#### Event Core with Extended Measurement or Fact
An innovation that OBIS made in this space was introducing the Extended Measurement or Fact extension (also sometimes referred to as OBIS-ENV-DATA). This uses the event core with an occurrence extension + the [extended measurement or fact extension](https://tools.gbif.org/dwca-validator/extension.do?id=http://rs.iobis.org/obis/terms/ExtendedMeasurementOrFact). This extension makes it possible to include measurements for both the events (salinity, temperature, dissolved oxygen, gear type, etc) as well as measurements about the occurrences (weight, length, etc). Prior to this you were only able to include measurements of the occurrence. 

<img width="800" alt="EventCoreSchema" src="https://obis.org/images/EventCoreSchema.png" style="background-color:white;" />

Over at the IOOS Bio Data Guide Github you can see [a script](https://github.com/ioos/bio_data_guide/blob/main/datasets/TPWD_HARC_BagSeine/TPWD_HARC_BagSeine_OBISENV.md) that was used to take data in it's original form and align it to Darwin Core Event Core with Extended Measurement or Fact.
<img width="555" alt="ProcessingScriptScreenshot" src="https://user-images.githubusercontent.com/7586150/148693542-00040e22-bce0-4123-8848-e97064c7027b.PNG">


{% include links.md %}
