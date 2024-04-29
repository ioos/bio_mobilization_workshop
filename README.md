# Marine Biological Data Mobilization Workshop 2023

Workshop Digital Object Identifiers (DOI):
| DOI | Year |
|-----|------|
| [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7401979.svg)](https://doi.org/10.5281/zenodo.7401979) | ALL |
| [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11085142.svg)](https://doi.org/10.5281/zenodo.11085142) | 2024 |
| [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7896606.svg)](https://doi.org/10.5281/zenodo.7896606) | 2023 |
| [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7401980.svg)](https://doi.org/10.5281/zenodo.7401980) | 2022 |

This repository is for participants to get general information and ask questions related to the Biological Data Mobilization Workshop (via the [issues](https://github.com/ioos/bio_mobilization_workshop/issues) section).

Marine Data Mobilization Workshop for Biology and Ecosystem Essential Ocean Variables (Bio-Eco EOV) is a Contribution to the UN Decade on Ocean Science for Sustainable Development and the Marine Life 2030 Decade Action. The workshop is jointly hosted by CIOOS, IOOS, Hakai, MBON, OBIS-USA, and OTN.

This workshop is a small hands-on, interactive virtual workshop focused on mobilizing marine biological observation datasets to the Ocean Biodiversity Information System (OBIS) by helping data providers standardize their data using Darwin Core. This includes species observations from any type of sampling methodologies (e.g. visual surveys, net tows, microscopy, fish trawls, imaging, 'omics, acoustics, telemetry).

Workshop website: https://ioos.github.io/bio_mobilization_workshop/

## Contributing

We welcome all contributions to improve the lesson! Maintainers will do their best to help you if you have any
questions, concerns, or experience any difficulties along the way.

We'd like to ask you to familiarize yourself with our [Contribution Guide](CONTRIBUTING.md) and have a look at
the [more detailed guidelines][lesson-example] on proper formatting, ways to render the lesson locally, and even
how to write new episodes.

Please see the current list of [issues][FIXME] for ideas for contributing to this
repository. For making your contribution, we use the GitHub flow, which is
nicely explained in the chapter [Contributing to a Project](http://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project) in Pro Git
by Scott Chacon.
Look for the tag ![good_first_issue](https://img.shields.io/badge/-good%20first%20issue-gold.svg). This indicates that the maintainers will welcome a pull request fixing this issue.  


## Maintainer(s)

Current maintainers of this lesson are 

* @MathewBiddle
* @7yl4r
* @albenson-usgs


## Authors

A list of contributors to the lesson can be found in [AUTHORS](AUTHORS)

## Citation

To cite this lesson, please consult with [CITATION](CITATION.cff)

## Deploying site locally
See [this documentation](https://carpentries.github.io/lesson-example/setup.html).

Navigate to the folder that contains the lesson, and use `bundle exec jekyll serve` to preview the lessons.

If changing headers and menus `bundle exec jekyll clean` before serving.

<!--## Post-mortem 2022 workshop summary
This workshop has concluded with great success! We hope to remix and offer another similar workshop soon! Below is a summary of the workshop activities prepared post-mortem, followed by the original content of this README which was written pre-workshop.

The 2022 Marine Biological Data Mobilization Workshop was a collaborative effort between OBIS, MBON, Hakai, IOOS, and OTN hosted to promote open data and software in the area of marine biodiversity assessment. The workshop focused on the application of the Darwin Core data standard to extant data and the subsequent publication of the data to the open access data infrastructures provided by OBIS and GBIF. The curriculum for this workshop was modeled using The Carpentries evidence-based best-practices of teaching. The materials are openly available via GitHub and the generated carpentries website. The workshop is licensed as free for re-use or adaptation under an MIT license. Unconventional features of the workshop included: 

1. A majority of workshop time allocated to breakout rooms and individual work
2. The use of concurrent, topical breakout rooms led by instructors in combination with “floating” specialist volunteers
3. A 100% open and free virtual workshop leveraging synchronous and asynchronous communications technologies including slack, zoom, and github
4. A dual-programming-language (python and R) offering in all instructional steps

The workshop was attended internationally by 63 participants, with 48 attendees joining the associated slack group. These new members have been invited to attend a monthly workgroup organized to promote standardization of marine biological data. A pre-vs-post survey analysis shows substantial improvement to self-reported skill-levels, a multitude of positive feedback was volunteered, and the workshop scored a perfect 100% standard Net Promoter Score with 16 “promoters”, 0 “detractors”, and a total of 25 respondents.
-->

## How this repo is organized

At the completion of each event, this repository will be tagged and a release will be created with the year of the event. A DOI will be minted through Zenodo (see DOI table above). Since the workshop is intended to provide the most up to date information on aligning data to Darwin Core, the maintainers decided that we will continually build and update these materials instead of providing access to the previous years materials in subsequent yearly websites. If you would like to rebuild a specific year's website, checkout a specific [release](https://github.com/ioos/bio_mobilization_workshop/releases) (eg. `$ git checkout 2023`) and [build the website](#deploying-site-locally) from that content.
