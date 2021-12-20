# Contributing

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

## How to Contribute
The easiest way to get started is to file an issue to tell us about a spelling mistake, some awkward wording,
or a factual error. This is a good way to introduce yourself and to meet some of our community members.

1. If you have a [GitHub][github] account, or are willing to [create one][github-join], but do not know how to use Git,
you can report problems or suggest improvements by [creating an issue][issues]. This allows us to assign the item 
to someone and to respond to it in a threaded discussion.

2. If you are comfortable with Git, and would like to add or change material, you can submit a pull request (PR).
Instructions for doing this are [included below](#using-github).

## Where to Contribute
Contribute your example datasets to the `datasets/` directory.
* Create a subdirectory for your dataset using a short name (eg. `south_pacific_zooplankton_1801/`)
  * This directory will contain all of the files associated with the workshop.
* Create a subdirectory for your data (eg. `south_pacific_zooplankton_1801/data/`)
* Create a subdirectories for raw and processed data (eg. `south_pacific_zooplankton_1801/data/raw/` and `south_pacific_zooplankton_1801/data/processed/`)
* All of your scripts and intermediary files should be stored in the root dataset directory (eg. `south_pacific_zooplankton_1801/`)

In the end your dataset directory should look something like:
```shell
└───south_pacific_zooplankton_1801
    │   processing.py
    │
    └───data
        ├───processed
        │       emof.csv
        │       event.csv
        │       occurrence.csv
        │
        └───raw
                raw_data.csv
```

## Using GitHub

If you choose to contribute via GitHub, you may want to look at [How to Contribute to an Open Source Project on 
GitHub][how-contribute]. To manage changes, we follow [GitHub flow][github-flow]. To use the web interface for 
contributing to a file:

1. Fork the originating repository to your GitHub profile.
2. Within your version of the forked repository, move to the `main` branch and create a new branch for each 
significant change being made.
3. Navigate to the file(s) you wish to change within the new branches and make revisions as required.
4. Commit all changed files within the appropriate branches.
5. Create individual pull requests from each of your changed branches to the `main` branch within the originating 
repository.
6. If you receive feedback, make changes using your issue-specific branches of the forked repository and the pull 
requests will update automatically.
7. Repeat as needed until all feedback has been addressed.

When starting work, please make sure your clone of the originating `main` branch is up-to-date before creating your own 
revision-specific branch(es) from there. Additionally, please only work from your newly-created branch(es) and *not*
your clone of the originating `main` branch.








[github]: https://github.com
[github-flow]: https://guides.github.com/introduction/flow/
[github-join]: https://github.com/join
[how-contribute]: https://app.egghead.io/playlists/how-to-contribute-to-an-open-source-project-on-github
[issues]: https://guides.github.com/features/issues/