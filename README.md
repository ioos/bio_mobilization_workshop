# Marine Biological Data Mobilization Workshop 2022
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

