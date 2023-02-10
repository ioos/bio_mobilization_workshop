---
layout: page
title: eDNA Extension
permalink: /edna-extension/
questions:
- "How should people use the DNA-derived data extension?"
- "Why should people the DNA-derived data extension?"
- "What are the required or highly recommended Darwin Core terms for sharing to OBIS?"
objectives:
- "Understand the purpose of the DNA-derived data extension."
- "Understand required or (highly) recommended fields needed in the extension, depending on analytical approach taken."
keypoints:
- "Ensure you know the objective of your study."
- "Define whether you have used metabarcoding or qPCR to determine (highly) recommended fields in the DNA-derived data extension."
---
* Table of contents
{:toc}

# eDNA Extension 

<https://docs.gbif.org/publishing-dna-derived-data/1.0/en/>

# Introduction
Target audience: data managers and data providers with basic understanding of genomic sequencing data looking to publish their DNA-derived data to OBIS or GBIF.

DNA-derived data enables us to record inconspicuous or otherwise unobservable taxa, and this type of data should be as standardized and reproducible as possible, regardless of whether or not the detected species have formal scientific names. DNA-derived data may come from well-documented sampling or individual organisms, may be backed by preserved physical material or not, and may result from genetic sequencing or other DNA detection methods, such as qPCR. DNA-derived biological occurrence data includes information derived from DNA from individual organisms, but also from environmental DNA (eDNA) and from bulk samples comprising many individuals. The number of DNA-derived datasets in OBIS is limited (currently only 26). Raw, pre-processed sequences files should be stored in external archives or repositories (e.g. GenBank, ENA), and can be assigned a taxon by comparing them against reference databases (libraries). When libraries are incomplete, sequence classification can be done without taxonomic identification, either by clustering sequences into operational taxonomic units (OTUs) or by denoising the data, producing amplicon sequence variants (ASVs). Standardizing DNA-derived occurrence data will help provide a mechanism to store occurrence records of undescribed species. It is recommended practice that processed data should be provided as an extension to the occurrence core/extension in the DwC-A schema. 	

With regards particularly to studying eDNA, there are two main analytical methods that exists which can generally be classified in two main classes: 

1. Those which aim to detect a specific organism (qPCR/ddPCR)
1. those which describe an assemblage or community of organisms (metabarcoding). 

For the detection of specific species in eDNA-samples, most analyses include species-specific primers and qPCR (Quantitative Polymerase Chain Reaction) or ddPCR (Droplet-Digital Polymerase Chain Reaction). These methods do not generate DNA-sequences, and the occurrence data are completely dependent on the specificity of primers or assays used, so this information is highly recommended to be provided. Metabarcoding utilizes general primers to generate a lot of DNA-sequences, which can be compared to a reference database (library), like GenBank, BOLD or UNITE. This comparison allows each DNA-sequence to be assigned to a species or higher rank taxon identity.

The efficacy of classification depends on the completeness (coverage) and the reliability of reference libraries, as well as the tools used to carry out the classification. These are all moving targets, making it essential to apply taxonomic expertise and caution in the interpretation of results. For increased reusability and reproducibility of genetic sequencing data, it is important to provide data users with information pertaining to e.g. the habitat where the sample was collected from, DNA sequence, primer used, targeted gene, and referencing the sampling protocol. Where applicable, providing the verified amplicon sequence variants ([Сallahan et al. 2017](https://doi.org/10.1038/ismej.2017.119)) allow for precise reinterpretation of data, intra-specific population genetic analyses ([Sigsgaard et al. 2019](https://doi.org/10.1038/s41559-016-0004)) and is likely to increase identification accuracy.

### Workflow
The following workflow diagram is taken from the GBIF DNA-derived data manuscript. We are mainly focusing on the lower half of this diagram, particularly in standardizing genomic data to DwC and providing proper referencing to protocols and other metadata required for understanding the context in which the data was collected. 

<figure>
  <img
       src = "https://docs.gbif.org/publishing-dna-derived-data/1.0/img/web/outline-of-a-platform.en.svg"
       alt = "DNA-derived data workflow">
  <figcaption>DNA-derived data workflow. In this workshop we will focus primarily on the Internal institutional data management and IPT / Darwin Core Archive boxes. Image is Figure 3 from: https://docs.gbif.org/publishing-dna-derived-data/1.0/img/web/outline-of-a-platform.en.svg.</figcaption>
</figure>

The DNA-derived extension is an extension in the DwC-A schema, and has to be used as an extension to an Occurrence Core (or extension) or Event Core. It can be used in combination with other extensions, such as the Measurement & Facts extension. Information included in the DNA-derived extension should make it easier for data users to understand, analyze or reuse your genomic occurrence data. The value in adding your DNA-sequence or genomic data to GBIF comes from associating spatio-temporal occurrence data and dna-based names from the DNA data. It helps provide a mechanism for storing occurrence records of undescribed species. When these species become linked to a Linnean name, all these linked occurrence records will be immediately available. Including this data in GBIF increases citability, can hasten its discovery and integration in biological conservation and policy-making. Specific granularity is required for accurate reproducibility, especially in a field where protocols used can vastly impact the taxa observed. 

### 5 Categories
Typically, molecular approaches to biodiversity characterization through qPCR and metabarcoding can be separated into 5 categories. Information collected in each of these categories can be included in the DNA-derived extension. 

- Category 1 (metabarcoding): DNA-derived occurrences = DNA sequence or detection through PCR is the only evidence for presence of a given organism or community
- Category 2 (metabarcoding): Enriched occurrences = if some genetic materials are, or can be, associated with an observation or a specimen (not the only evidence of occurrences).
- Category 3 (qPCR): Targeted species detection (qPCR/ddPCR) = data where a specific (qPCR/ddPCR) assay is used to detect presence/absence of DNA sequence specific to target organism.
- Category 4 (metabarcoding): Name references (e.g. iBOL) = DNA-derived names, derived from clustering (OTU) or denoising (ASV)
- Category 5 (metabarcoding).: Metadata-only datasets

See for a decision tree [Table 1](https://docs.gbif.org/publishing-dna-derived-data/1.0/en/). For examples of datasets in GBIF for each of these categories see sections 2.1.1. - 2.1.5.  

### Tables 
When dealing with Metabarcoding or qPCR data, it is (highly) recommended that aside from the general required fields in DwC (covered in section 1 of our data mobilization workshop) the following fields are included: These fields are free-text. The DNA-derived data extension will have different requirements based on the analytical method applied in your project (i.e. metabarcoding vs. qPCR). 

Table x. Recommended fields for Occurrence core or extension. An extended version of this table is found in [GBIF manual](https://docs.gbif-uat.org/publishing-dna-derived-data/1.0/en/#mapping-metabarcoding-edna-and-barcoding-data).

| | Metabarcoding                ||             qPCR                    ||
| :----------------|:------------|:----------|:-------------|:----------|
| **Darwin Core Term** | **Description** | **Required**  | **Description**  |  **Required** |
| [`organismQuantity`](https://dwc.tdwg.org/terms/#dwc:organismQuantity) | Number of reads of this sequence variant in the sample | Highly recommended | Number of positive droplets/chambers in the sample | Highly recommended | 
| [`organismQuantityType`](https://dwc.tdwg.org/terms/#dwc:organismQuantityType) | Should always be **DNA sequence reads** | Highly recommended | The partition type | Highly recommended |
| [`sampleSizeValue`](https://dwc.tdwg.org/terms/#dwc:sampleSizeValue) | Total number of reads in the sample. This important since it allows calculating the relative abundance of the sequence variant within the sample | Highly recommended | The number of accepted partitions (n), e.g. meaning accepted droplets in ddPCR or chambers in dPCR. | Highly recommended |
| [`sampleSizeUnit`](https://dwc.tdwg.org/terms/#dwc:sampleSizeUnit) | Should always be **DNA sequence reads** | Highly recommended | The partition type, should be equal to the value in organismQuantityType | Highly recommended |
| [`materialSampleID`](https://dwc.tdwg.org/terms/#dwc:materialSampleID) | An identifier for the MaterialSample (as opposed to a particular digital record of the material sample). Use the biosample ID if one was obtained from a nucleotide archive. In the absence of a persistent global unique identifier, construct one from a combination of identifiers in the record that will most closely make the materialSampleID globally unique. | Highly recommended | An identifier for the MaterialSample (as opposed to a particular digital record of the material sample). Use the biosample ID if one was obtained from a nucleotide archive. In the absence of a persistent global unique identifier, construct one from a combination of identifiers in the record that will most closely make the materialSampleID globally unique. | Highly recommended |
| [`samplingProtocol`](https://dwc.tdwg.org/terms/#dwc:samplingProtocol) | The name of, or reference to, or description of the method or protocol used during the sampling event.  | Recommended | The name of, or reference to, or description of the method or protocol used during the sampling event. | Recommended |
| [`taxonID`](https://dwc.tdwg.org/terms/#dwc:taxonID) | For eDNA data, it is recommended to use an MD5 hash of the sequence and prepend it with **ASV**.  | Highly recommended if DNA_sequence is not provided |  |  |
| [`scientificName`](https://dwc.tdwg.org/terms/#dwc:scientificName) |  |  | Latin name of the closest known taxon (species or higher) or an OTU identifier from BOLD or UNITE | **Required** |


Table x. Recommended fields from the DNA derived data extension when handling metabarcoding data.. An extended version of this table is found in GBIF manual.

| Darwin Core Term | Description | Required | 
|------------------|------------------------------------|--------------------------------------- |
| [`DNA_sequence`](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2021-07-05.xml#DNA_sequence) | The DNA sequence (ASV). | Highly recommended | 
| [`sop`](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2021-07-05.xml#sop) | Standard operating procedures used in assembly and/or annotation of genomes, metagenomes or environmental sequences (e.g. through protocols.io) | Recommended | 
| [`target_gene`](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2021-07-05.xml#target_gene) | Targeted gene or marker name for marker-based studies | Highly recommended | 
| [`target_subfragment`](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2021-07-05.xml#target_gene) | Name of subfragment of a gene or markerImportant to e.g. identify special regions on marker genes like the hypervariable V6 region of the 16S rRNA gene | Highly recommended | 
| [`pcr_primer_forward`](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2021-07-05.xml#pcr_primer_forward) | Forward PCR primer that was used to amplify the sequence of the targeted gene, locus or subfragment. | Highly recommended | 
| [`pcr_primer_reverse`](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2021-07-05.xml#pcr_primer_reverse) | Reverse PCR primer that was used to amplify the sequence of the targeted gene, locus or subfragment.  | Highly recommended | 
| [`pcr_primer_name_forward`](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2021-07-05.xml#pcr_primer_name_forward) | Name of the forward PCR primer | Highly recommended |
| [`pcr_primer_name_reverse`](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2021-07-05.xml#pcr_primer_name_reverse) | Name of the reverse PCR primer | Highly recommended |
| [`pcr_primer_reference`](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2021-07-05.xml#pcr_primer_reference) | Reference for the primers | Highly recommended |

Table x. Recommended fields from the DNA derived data extension when handling qPCR data (Cat 3). An extended version of this table is found in GBIF manual.

| Darwin Core Term | Description | Required | 
|------------------|------------------------------------|--------------------------------------- |
| [`sop`](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2021-07-05.xml#sop) | Standard operating procedures used in assembly and/or annotation of genomes, metagenomes or environmental sequences. A reference to a well documented protocol, e.g. using protocols.io | Highly recommended | 
| [`annealingTemp`](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2021-07-05.xml#annealingTemp) | The reaction temperature during the annealing phase of PCR. | Required if annealingTemp was supplied | 
| [`annealinTempUnit`](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2021-07-05.xml#annealingTempUnit) |  | Highly recommended | 
| [`pcr_cond`](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2021-07-05.xml#pcr_cond) | Description of reaction conditions and components of PCR in the form of "initial denaturation:94degC_1.5min; annealing=…" | Highly recommended | 
| [`probeReporter`](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2021-07-05.xml#probeReporter) | Type of fluorophore (reporter) used. Probe anneals within amplified target DNA. Polymerase activity degrades the probe that has annealed to the template, and the probe releases the fluorophore from it and breaks the proximity to the quencher, thus allowing fluorescence of the fluorophore. | Highly recommended | 
| [`probeQuencher`](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2021-07-05.xml#probeQuencher) | Type of quencher used. The quencher molecule quenches the fluorescence emitted by the fluorophore when excited by the cycler’s light source as long as fluorophore and the quencher are in proximity, quenching inhibits any fluorescence signals.  | Highly recommended | 
| [`ampliconSize`](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2021-07-05.xml#ampliconSize) | The length of the amplicon in basepairs | Highly recommended |
| [`thresholdQuantificationCycle`](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2021-07-05.xml#thresholdQuantificationCycle) | Threshold for change in fluorescence signal between cycles | qPCR: Highly recommended |
| [`baselineValue`](https://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2021-07-05.xml#baselineValue) | The number of cycles when fluorescence signal from the target amplification is below background fluorescence not originated from the real target amplification. | qPCR: Highly recommended |

It is recommended that if ASVs are provided, MD5s should be generated by the biodiversity discovery platforms. If ASVs are not provided, the MD5s need to be mandatory. This will help data platform index actual sequences, or at the very minimum a MD5 checksum of these to facilitate searches for ASVs across datasets. 

## References
1. Andersson AF, Bissett A, Finstad AG, Fossøy F, Grosjean M, Hope M, Jeppesen TS, Kõljalg U, Lundin D, Nilsson RN, Prager M, Svenningsen C & Schigel D (2021) Publishing DNA-derived data through biodiversity data platforms. v1.0 Copenhagen: GBIF Secretariat. https://doi.org/10.35035/doc-vf1a-nr22.
1. [The OBIS Manual](https://manual.obis.org/examples.html)
3. [Schema for DNA-Derived Data Extension](http://rs.gbif.org/extension/gbif/1.0/dna_derived_data_2021-07-05.xml)

## Example Datasets
1. [18S Monterey Bay Time Series: an eDNA data set from Monterey Bay, California, including years 2006, 2013 - 2016](https://obis.org/dataset/62b97724-da17-4ca7-9b26-b2a22aeaab51)
1. [eDNA metabarcoding survey of tropical north‐western Australia, Indian Ocean (2017-2018)](https://obis.org/dataset/51c555be-c3e8-49de-9299-6f08f029002c)

## Relevant R/Python packages
R: 
  - [DADA2: processing sequences to ASVs and more](https://benjjneb.github.io/dada2/)
  - [Phyloseq: tool to import, store, analyze, and graphically display complex phylogenetic sequencing data after clustering](https://joey711.github.io/phyloseq/)

Python:
  - https://github.com/biocore/biom-format 
  - https://entrezpy.readthedocs.io/en/master/ 


