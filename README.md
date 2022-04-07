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

--------------------------------------------------------------------------------
## myBinder environments
Below are the links to myBinder environments for Python and R as well as RStudio. These links will initialize a [JupyterHub](https://jupyterhub.readthedocs.io/en/latest/) server which will host this repository's contents. You can start a script to process your data within this environment and save your script/notebook file to your local system.

Jupyter R+Python: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ioos/bio_mobilization_workshop/main) 

RStudio: [![RStudio](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ioos/bio_mobilization_workshop/main?urlpath=rstudio)

_Caution_ Initially it will take a little while to build the environment in mybinder. Be patient.

**Note** The repository was changed from `ocean_sciences_bio_workshop_2021` to `bio_mobilization_workshop`.

--------------------------------------------------------------------------------
## How this repo is organized

### Branch structure
- `gh-pages` - website materials for the current workshop
  - **_episodes/** - directory where markdown files are for the website.
- `main` - datasets/code for the current workshop
  - **datasets/** - directory containing example data and scripts for darwin core alignment

Archived material will be stored in a branch indicating the year and material. For example, the 
2022 website material will be archived in the branch `2022_site` (or `2022_gh-pages`?). The 2022 workshop datasets/code 
will be archived in the branch `2022_main`. This ensures all material is accessible in the future and facilitates 
replicating the materials for another workshop.

