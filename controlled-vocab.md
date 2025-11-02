---
layout: page
title: Controlled Vocabulary
permalink: /controlled-vocab/
---

:::::::::::: questions

- What is controlled vocabulary?
- Why should we use it?
- How do we choose and use controlled vocabulary in our data?

::::::::::::::::::::::

::::::::::: objectives

- Understand the purpose of controlled vocabulary
- Understand the basics of how to find and select a vocabulary term for the eMoF table
- Learn how to populate measurementTypeID, measurementValueID, and measurementUnitID

::::::::::::::::::::::

## Introduction

Controlled vocabulary is simply the use of a standardized and defined set of terms to populate or describe data. This could include specific data column names, a set of specific terms within a field, and the use of identifiers that point to a defined term. For the purposes of this workshop, we focus on using controlled vocabulary as identifiers in the extendedMeasurementOrFact (eMoF) extension table.

As we have learned in Episode 4: Darwin Core and Extension Schemas, the eMoF terms `measurementType`, `measurementValue`, and `measurementUnit` are completely unconstrained and can be populated with **free text**. While free text offers the advantage of capturing complex and unclassified information, there is inevitable semantic **heterogeneity** (e.g., of spelling, wording, or language) that becomes a challenge for effective data interoperability and analysis.

For example, if you were interested in finding all records related to weight measurements, you would have to try to account for all the different ways "weight" was recorded by data providers (weight, wgt, Weight, wet weight, dry weight, etc.). This is where using controlled vocabulary in the `measurementTypeID`, `measurementValueID`, and `measurementUnitID` fields is helpful! These 3 identifier fields are used to standardize measurement types, values and units. Identifiers used in these columns are populated with **Unique Resource Identifiers (URIs)** that provide clear and unambiguous definitions of the data.

Using URIs mean that if you call the `measurementType` "abundance" but I call it "Abundance per square meter" and we both use the `measurementTypeID` "<http://vocab.nerc.ac.uk/collection/P01/current/SDBIOL02/>" then we know this is the same measurement type even if we didn't use the same words to describe it. Choosing the right URI can be difficult but we will provide some basic guidance on this page. More details on controlled vocabulary and finding codes can be found in the [OBIS Manual](https://manual.obis.org/vocabulary.html).

## Why use controlled vocabulary?

Using controlled vocabulary will:

- ensure datasets are **consistently** documented
- simplify **data aggregation** and analysis of measurements
- decrease the potential that data will be **misunderstood or misused**

Controlled vocabularies are also important to ensure data are **interoperable** - readable by both humans and machines - and that the information is presented in an unambiguous manner. Vocabulary collections like the [NERC Vocabulary Server (NVS)](https://vocab.nerc.ac.uk/) compile vocabularies from different institutions and authorities (e.g., ISO, ICES, EUNIS), allowing you to map your data to them. OBIS recommends selecting terms from NVS whenever possible, but other vocabulary collections may be used (e.g. ICES, EcoPortal, ENVO, etc.) as long as the URIs provided are machine readable and interoperable.

When we all correctly use controlled vocabulary with our measurement data, we can search for a single `measurementTypeID` and obtain all related records, regardless of differences in wording or language used in the data.

:::::::::::: callout

## :pushpin: Tip

You can search for `measurementTypes` that other OBIS data providers have used by using the [OBIS Mof Viewer](https://mof.obis.org/). **BE CAREFUL** when using this tool and make sure the definition in the URI matches exactly your measurement type if you want to reuse it for your data.

::::::::::::::::::::

## How to select controlled vocabulary?

Where do we start when selecting controlled vocabularies? As mentioned above, OBIS strongly recommends selecting terms from the NERC Vocabulary Server. If your institution already recommends a machine-readable vocabulary collection, it is okay to continue using that, as long as the URIs are publicly accessible and machine-readable.

When selecting a vocabulary term keep in mind these general principles:

- machine operable (URI, IRI)
- human readable
- clear, unambiguous definitions
  
OBIS has created a [**decision tree**](https://manual.obis.org/vocab_tree.html) and has released [video tutorials](https://www.youtube.com/watch?v=gGiSTApx1oU&list=PLlgUwSvpCFS4hADB7Slf44V1KJauEU6Ul) to help with choosing URIs. While we won't go over the decision tree in detail here, you can watch the video series for additional assistance.

For now, let's break it down for each of the measurement ID columns in the eMoF, starting with the "simplest" column.

### measurementUnitID

The `measurementUnitID` field is the easiest measurement ID field to populate. It is used to provide a URI for the **unit** associated with the value provided to `measurementValue` (e.g. cm, kg, kg/m^2). OBIS recommends this field be populated with terms from the **NVS P06 collection**, *BODC-approved data storage units*. See screenshot below for an example vocabulary term from this collection, and where to find the URI on the page.

![Screenshot of a unit within the NVS P06 collection. Box highlights the URI to be used in measurementUnitID field.](/episodes/fig/NVS_unit-box.png)

To search this collection, see **<https://www.bodc.ac.uk/resources/vocabularies/vocabulary_search/P06/>**.

Other examples for `measurementUnit` and associated `measurementUnitID` include:

- Metres: <http://vocab.nerc.ac.uk/collection/P06/current/ULAA/>
- Days: <http://vocab.nerc.ac.uk/collection/P06/current/UTAA/>
- Metres per second: <http://vocab.nerc.ac.uk/collection/P06/current/UVAA/>
- Percent: <http://vocab.nerc.ac.uk/collection/P06/current/UPCT/>
- Milligrams per litre: <http://vocab.nerc.ac.uk/collection/P06/current/UMGL/>

### measurementValueID

The `measurementValueID` field is used to provide an identifying code when `measurementValue` is populated with **non-numerical values** (e.g. sampling related, sex or life stage designation, etc.).

:::::::::::: callout

`measurementValueID` is NOT used for standardizing numeric measurements!

::::::::::::

Unlike `measurementUnitID`, there are **multiple NVS collections** that may be used to search for and select terms from. The collection is dependent on which type of `measurementValue` you have. See the table below for some common, non-exhaustive examples. Note that when documenting behaviour values in the eMoF, OBIS recommends using codes from the [**ICES Vocabulary Server**](https://vocab.ices.dk/).

| Type of measurementValue | Vocabulary Collection |
|--------------------------|------------|
|Sex (gender)| [S10](https://www.bodc.ac.uk/resources/vocabularies/vocabulary_search/S10/) |
|Lifestage | [S11](https://www.bodc.ac.uk/resources/vocabularies/vocabulary_search/S11/) |
|Sampling instruments and sensors (SeaVoX Device Catalogue)| [L22](https://www.bodc.ac.uk/resources/vocabularies/vocabulary_search/L22/) |
|Sampling instrument categories (SeaDataNet device categories) | [L05](https://www.bodc.ac.uk/resources/vocabularies/vocabulary_search/L05/) |
|Vessels (ICES Platform Codes) | [C17](https://www.bodc.ac.uk/resources/vocabularies/vocabulary_search/C17/) |
| European Nature Information System Level 3 Habitats | [C35](https://www.bodc.ac.uk/resources/vocabularies/vocabulary_search/C35/) |
| Behaviour | [ICES Behaviour collection](https://vocab.ices.dk/?codetypeguid=d0268a96-afc9-436e-a4db-4f61c2b9f6ba) |

You may also populate `measurementValueID` with references to papers or manuals that document, for example, the sampling protocol used to obtain the measurement. To do this you should use either:

- The DOI of a paper or manual
- Handle for publications on IOC’s Ocean Best Practices repository, e.g. <http://hdl.handle.net/11329/304>

### measurementTypeID

This is likely the most important, yet most difficult column to populate. It is the field that provides the URI defining your measurement or fact, and is most likely to be used to filter and aggregate measurement data in OBIS. Therefore it is important to do your best to select the **most appropriate** vocabulary term that best defines all important elements related to your measurement. Important elements may include:

- the property or attribute being measured
- the object or entity of interest (e.g. a chemical, a biological organism)
- the environmental context of the measurement (e.g. per unit volume, per unit area)
- specific methods required to interpret, understand, or contextualize the measurement (e.g. optical microscopy, filtration, computation, correction algorithms)

Think about what information a user would need to know in order to reuse your measurement data, then try to find a vocabulary term that includes all those measurements. Not all of the above may be necessary to include in your vocabulary term.

OBIS recommends selecting a vocabulary term from the **NVS P01 collection**. This is because the terms in this collection are built on a semantic structure that allows the elements listed above to be directly included in the vocabulary term. While you can search for terms in this collection at <https://vocab.nerc.ac.uk/search_nvs/P01/>, we strongly suggest using the **[SeaDataNet Facet Search](https://vocab.seadatanet.org/p01-facet-search)**, which is a bit more user friendly to use.

Here are a few examples of vocabulary terms mapped to the P01 collection:

- Description of sub-sampling protocol: <https://vocab.nerc.ac.uk/collection/P01/current/DSPSSP01/>
- Length of sampling track <https://vocab.nerc.ac.uk/collection/P01/current/LENTRACK/>
- Height of sample collector (e.g. a grab) <https://vocab.nerc.ac.uk/collection/P01/current/MTHHGHT1/0>
- Name of sampling instrument <https://vocab.nerc.ac.uk/collection/P01/current/NMSPINST/>
- Sample duration <https://vocab.nerc.ac.uk/collection/P01/current/AZDRZZ01/>

## Requesting new vocabulary terms

If you are unable to find a suitable vocabulary term for any of your measurementType, measurementValue, or measurementUnit, then you can **request a suitable term be created** for you. To do this, you can submit a request through the **OBIS Vocabulary GitHub repository** (<https://github.com/nvs-vocabs/OBISVocabs/issues>).

If you are unsure about whether a code fits your specific case, please feel free to ask questions in the Vocab channel on the OBIS Slack, or in the SMBD Slack.

::::::::::::: keypoints

- Controlled vocabulary ensures datasets are consistently documented, simplifies data aggregation, and can decrease data misuse
- OBIS recommends populating measurementTypeID, measurementValueID, and measurementUnitID with terms from the NERC Vocabulary Server
- Other vocabulary terms may be used as long as the URIs are machine readable
- You can request new vocabulary terms to be created through the OBIS Vocab GitHub repository

:::::::::::::::::::::::
