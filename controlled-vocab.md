---
layout: page
title: Controlled Vocabulary
permalink: /controlled-vocab/
---

:::::::::::: questions

- What is controlled vocabulary?
- Why should we use it?
- How do we use and choose controlled vocabulary in our data?

::::::::::::::::::::::

::::::::::: objectives

- Understand the purpose of the DNA-derived data extension.
- Understand required or (highly) recommended fields needed in the extension, depending on analytical approach taken.

::::::::::::::::::::::

## Introduction

Controlled vocabulary is simply the use of a standardized set of terms to populate or describe data. This could include specific data fields,
It even includes (technically) the use of DwC terms in our header columns!

As we have learned earlier in this course, the extendedMeasurementOrFact (eMoF) terms measurementType, measurementValue, and measurementUnit are completely unconstrained and can be populated with free text. While free text offers the advantage of capturing complex and unclassified information, there is inevitable semantic heterogeneity (e.g., of spelling, wording, or language) that becomes a challenge for effective data interoperability and analysis.

For example, if you were interested in finding all records related to weight measurements, you would have to try to account for all the different ways “weight” was recorded by data providers (weight, wgt, Weight, wet weight, dry weight, etc.).

## Why?

Controlled vocabularies are incredibly important to ensure data are **interoperable** - readable by both humans and machines - and that the information is presented in an unambiguous manner. Vocabulary collections like NVS compile vocabularies from different institutions and authorities (e.g., ISO, ICES, EUNIS), allowing you to map your data to them. In this way, you could search for a single measurementTypeID and obtain all related records, regardless of differences in wording or language used in the data.

## How?

When selecting keep in mind these principles:

- machine operable (IRI, URI)
- standardized terms
- human readable
  
Let's break it down for each of the measurement ID columns in the eMoF, starting with the "simplest" column

### measurementUnitID

### measurementValueID

### measurementTypeID
