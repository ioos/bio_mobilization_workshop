---
title: 'Reference'
---

## Glossary

**Core table**: The main file in a Darwin Core-Archive and can be linked to extension tables through the use of identifiers. Can be Event, Occurrence, or Taxon (for GBIF). 

**Darwin Core**: A standard to facilitate the sharing of biological diversity information. Includes a glossary of terms based on taxa, their occurrence in nature as documented by observations, specimens, samples, and related information. This is one of the main standards that OBIS adheres to.

**Ecological Metadata Language (EML)**:
XML syntax for documenting metadata about research data. For more details see https://eml.ecoinformatics.org/

**Event table**:
Data table that contains information about the sampling event, including location, time/date, and sampling protocols. Each row is a unique event with a unique eventID. Allows for hierarchical event structure by nesting events into parent events with parentEventID.

**eventID**:
A unique, persistent identifier for an individual sampling or observation event. Can be constructed with information from the data, e.g. [project]:[year or date]:[location]:[site]_[sample] STAR_1989-04-04_arcticsea_st3520_s01. When relevant, eventIDs must be connected to a parentEventID.


**ExtendedMeasurementOrFact (eMoF) table**:
Table used to record all measurements related to the events in an Event table, and/or occurrence recorded in the OCcurence table. Measurements are linked to records using eventID and occurrenceIDs, respectively. Measurement data is recorded in "long" format where the fields measurementType, measurementValue, and measurementUnit are used. Best practice is to also populate measurement IDs for each field.

**Extension table**:
A data table linked to the core table by identifiers. Can be Occurrence, ExtendedMeasurementOrFact, or DNA-Derived data.

**Identifiers**:
A unique, persistent identifier used to distinguish each event, occurrence, physical sample, subsample, measurement, etc. in a dataset. Often constructed from elements in the data to create globally unique identifying strings, or can be generated. Examples include but are not limited to eventID, parentEventID, occurrenceID, measurement IDs: measurementTypeID, measurementUnitID, measurementValueID.

**Integrated Publishing Toolkit (IPT)**:
An open source web application that can be customized by the OBIS node manager and is used to publish and register all datasets. IPTs assist users to map data files to Darwin Core terms, and will archive + compress files into a Darwin Core Archive.

**Measurement Identifiers**:
Identifiers to standardize the measurement types, values and units used in the eMoF table. Helps to account for semantic heterogeneity in how measurement data is recorded, allowing for users to identify all measurement data of interest with a single identifier. Includes measurementTypeID, measurementValueID, and measurementUnitID

**NERC Vocabulary Server (NVS)**:
Server that gives access to standardised and hierarchically-organized vocabularies that can be used for identifiers. It is managed by the British Oceanographic Data Centre at the National Oceanography Centre (NOC) in Liverpool. Vocabularies are organized into thematic collections, e.g. P01, P06 collections.

**Occurrence table**:
Table that contains information on the biological occurrences, including taxonomy. Each record contains the observation of one organism. Must indicate the type of observation in basisOfRecord (e.g. PreservedSpecimen, FossilSpecimen, LivingSpecimen, MaterialSample, HumanObservation, MachineObservation).

**occurrenceID**:
An identifier for an occurrence record, must be globally unique and persistent. Example STAR_arcticsea_st3520_1989-04-04_s01_BoSai_1

**Ocean Biodiversity Information System (OBIS)**:
The most comprehensive repository for the world’s ocean biodiversity and biogeographic data and information. Provides open access to quality-controlled marine biodiversity data.

**P01 code**:
A concept from the NERC Vocabulary Server P01 collection. These codes should be used to populate the measurementTypeID field.

**parentEventID**:
An identifier for a parent event, which is composed of one or more sub-sampling (child) events. Must be persistent and unique. Example: STAR_1989_arcticsea

**scientificNameID**: A strongly recommended term for OBIS data which contains an identifier for a scientific name. The identifier provided to this field must correspond with the name in the scientificName field. Suggested to be populated with LSIDs from WoRMS, but ITIS, BOLD, and NCBI identifiers are also accepted.

**World Register of Marine Species (WoRMS)**: An authoritative and comprehensive list of names of marine organisms, including information on synonymy. The taxonomic backbone for OBIS. Life Science Identifiers (LSIDs) obtained from WoRMS are used to populate the scientificNameID field.