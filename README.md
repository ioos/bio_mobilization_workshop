# Marine Biological Data Mobilization Workshop

Workshop Digital Object Identifiers (DOI):
| DOI | Year |
|-----|------|
| [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7401979.svg)](https://doi.org/10.5281/zenodo.7401979) | ALL |
| [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18087438.svg)](https://doi.org/10.5281/zenodo.18087438) | 2025 |
| [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11085142.svg)](https://doi.org/10.5281/zenodo.11085142) | 2024 |
| [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7896606.svg)](https://doi.org/10.5281/zenodo.7896606) | 2023 |
| [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7401980.svg)](https://doi.org/10.5281/zenodo.7401980) | 2022 |

This repository is for participants to get general information and ask questions related to the Biological Data Mobilization Workshop (via the [issues](https://github.com/ioos/bio_mobilization_workshop/issues) section).

Marine Data Mobilization Workshop for Biology and Ecosystem Essential Ocean Variables (Bio-Eco EOV) is a Contribution to the UN Decade on Ocean Science for Sustainable Development and the Marine Life 2030 Decade Action. The workshop is jointly hosted by CIOOS, IOOS, Hakai, MBON, OBIS Secretariat, OBIS-USA, and OTN.

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

## How this repo is organized

At the completion of each event, this repository will be tagged and a release will be created with the year of the event (following [Calendar Versioning](https://calver.org/) scheme `YYYY`]). 
A DOI will be minted through Zenodo (see DOI table above). 
Since the workshop is intended to provide the most up to date information on aligning data to Darwin Core, the maintainers decided that we will continually build and update these materials instead of providing access to the previous years materials in subsequent yearly websites. 
If you would like to rebuild a specific year's website, checkout a specific [release](https://github.com/ioos/bio_mobilization_workshop/releases) (eg. `$ git checkout 2023`) and [build the website](#deploying-site-locally) from that content.


# Marine Biological Data Mobilization Workshop 2022
## Post-mortem summary
This workshop has concluded with great success! We hope to remix and offer another similar workshop soon! Below is a summary of the workshop activities prepared post-mortem, followed by the original content of this README which was written pre-workshop.

The 2022 Marine Biological Data Mobilization Workshop was a collaborative effort between OBIS, MBON, Hakai, IOOS, and OTN hosted to promote open data and software in the area of marine biodiversity assessment. The workshop focused on the application of the Darwin Core data standard to extant data and the subsequent publication of the data to the open access data infrastructures provided by OBIS and GBIF. The curriculum for this workshop was modeled using The Carpentries evidence-based best-practices of teaching. The materials are openly available via GitHub and the generated carpentries website. The workshop is licensed as free for re-use or adaptation under an MIT license. Unconventional features of the workshop included: 

1. A majority of workshop time allocated to breakout rooms and individual work
2. The use of concurrent, topical breakout rooms led by instructors in combination with “floating” specialist volunteers
3. A 100% open and free virtual workshop leveraging synchronous and asynchronous communications technologies including slack, zoom, and github
4. A dual-programming-language (python and R) offering in all instructional steps

The workshop was attended internationally by 63 participants, with 48 attendees joining the associated slack group. These new members have been invited to attend a monthly workgroup organized to promote standardization of marine biological data. A pre-vs-post survey analysis shows substantial improvement to self-reported skill-levels, a multitude of positive feedback was volunteered, and the workshop scored a perfect 100% standard Net Promoter Score with 16 “promoters”, 0 “detractors”, and a total of 25 respondents.


------------------------------------------------------------------------------

This repository is for participants to get general information and ask questions related to the Biological Data Mobilization Workshop (via the [issues](https://github.com/ioos/bio_mobilization_workshop/issues) section).

Marine Data Mobilization Workshop for Biology and Ecosystem Essential Ocean Variables (Bio-Eco EOV) is a Contribution to the UN Decade on Ocean Science for Sustainable Development and the Marine Life 2030 Decade Action. The workshop is jointly hosted by CIOOS, IOOS, Hakai, MBON, OBIS-USA, and OTN.

This workshop is a small hands-on, interactive virtual workshop focused on mobilizing marine biological observation datasets to the Ocean Biodiversity Information System (OBIS) by helping data providers standardize their data using Darwin Core. This includes species observations from any type of sampling methodologies (e.g. visual surveys, net tows, microscopy, fish trawls, imaging, 'omics, acoustics, telemetry).

Workshop website: https://ioos.github.io/bio_mobilization_workshop/

----
# The Carpentries Workbench Template Markdown Lesson

This lesson is a template lesson that uses [The Carpentries Workbench][workbench]. 

## Note about lesson life cycle stage
Although the `config.yaml` states the life cycle stage as pre-alpha, **the template is stable and ready to use**. 
The life cycle stage is preset to `"pre-alpha"` as this setting is appropriate for new lessons initialised using the template.

## Create a new repository from this template

To use this template to start a new lesson repository, 
make sure you're logged into Github.   
Visit https://github.com/carpentries/workbench-template-md/generate
and follow the instructions.
Checking the 'Include all branches' option will save some time waiting for the first website build
when your new repository is initialised.

If you have any questions, contact [@tobyhodges](https://github.com/tobyhodges)

## Configure a new lesson

Follow the steps below to
complete the initial configuration of a new lesson repository built from this template:

1. **Make sure GitHub Pages is activated:**
   navigate to _Settings_,
   select _Pages_ from the left sidebar,
   and make sure that `gh-pages` is selected as the branch to build from.
   If no `gh-pages` branch is available, check _Actions_ to see if the first
   website build workflows are still running.
   The branch should become available when those have completed.
1. **Adjust the `config.yaml` file:**
   this file contains global parameters for your lesson site.
   Individual fields within the file are documented with comments (beginning with `#`)
   At minimum, you should adjust all the fields marked 'FIXME':
   - `title`
   - `created`
   - `keywords`
   - `life_cycle` (the default, _pre-alpha_, is the appropriate for brand new lessons)
   - `contact`
1. **Annotate the repository** with site URL and topic tags:
   navigate back to the repository landing page and
   click on the gear wheel/cog icon (similar to ⚙️) 
   at the top-right of the _About_ box.
   Check the "Use your GitHub Pages website" option,
   and [add some keywords and other annotations to describe your lesson](https://cdh.carpentries.org/the-carpentries-incubator.html#topic-tags)
   in the _Topics_ field.
   At minimum, these should include:
   - `lesson`
   - the life cycle of the lesson (e.g. `pre-alpha`)
   - the human language the lesson is written in (e.g. `deutsch`)
1. **Adjust the 
   `CITATION.cff`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, and `LICENSE.md` files**
   as appropriate for your project.
   -  `CITATION.cff`:
      this file contains information that people can use to cite your lesson,
      for example if they publish their own work based on it.
      You should [update the CFF][cff-sandpaper-docs] now to include information about your lesson,
      and remember to return to it periodicallt, keeping it updated as your
      author list grows and other details become available or need to change.
      The [Citation File Format home page][cff-home] gives more information about the format,
      and the [`cffinit` webtool][cffinit] can be used to create new and update existing CFF files.
   -  `CODE_OF_CONDUCT.md`: 
      if you are using this template for a project outside The Carpentries,
      you should adjust this file to describe 
      who should be contacted with Code of Conduct reports,
      and how those reports will be handled.
   -  `CONTRIBUTING.md`:
      depending on the current state and maturity of your project,
      the contents of the template Contributing Guide may not be appropriate.
      You should adjust the file to help guide contributors on how best
      to get involved and make an impact on your lesson.
   -  `LICENSE.md`:
      in line with the terms of the CC-BY license,
      you should ensure that the copyright information 
      provided in the license file is accurate for your project.
1. **Update this README with 
   [relevant information about your lesson](https://carpentries.github.io/lesson-development-training/collaborating-newcomers.html#readme)**
   and delete this section.

[cff-home]: https://citation-file-format.github.io/
[cff-sandpaper-docs]:  https://carpentries.github.io/sandpaper-docs/editing.html#making-your-lesson-citable
[cffinit]: https://citation-file-format.github.io/cff-initializer-javascript/
[workbench]: https://carpentries.github.io/sandpaper-docs/

