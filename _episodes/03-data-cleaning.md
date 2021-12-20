---
title: "Data Cleaning"
teaching: 0
exercises: 3
questions:
- "How do I clean my data?"
objectives:
- "Getting your dates in order."
- "Matching scientific names to WoRMS."
- "Getting latitude and longitude to decimal degrees."
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"
---

# Getting your dates in order

> ## Exercise
> 
> Challenge: Convert the following dates to ISO-8601
> 
> 1. 01/31/2021 17:00 GMT
> 2. 31/01/2021 12:00 EST
> 3. January, 01 2021 5:00 PM GMT
> 4. noon Jan 01, 2021 EST 
> 5. 1612112400 seconds since 1970
> 
> > ## Solution
> > 1. 2021-01-31T1700Z
> > 2. 2021-01-31T1700Z
> > 3. 2021-01-31T1700Z
> > 4. 2021-01-31T1700Z
> > 5. 2021-01-31T1700Z
> > 
> > {: .output}
> {: .solution}
{: .challenge}

# Matching your scientific names to WoRMS
> ## Exercise
> 
> Challenge: Match the following names to a taxonomic authority.
> 
> - Great white shark
> 
> > ## Solution
> > - [Great White Shark](https://www.marinespecies.org/aphia.php?p=taxdetails&id=105838)
> >   - AphiaID - `urn:lsid:marinespecies.org:taxname:105838`
> > {: .output}
> {: .solution}
{: .challenge}



# Getting lat/lon to decimal degrees
> ## Exercise
> 
> Challenge: Convert the following latitude and longitude values to decimal degrees north and east, respectively.
> 
> 1. `17°51'57.96"S` `149°39'13.32"W` 
> 
> 
> > ## Solution
> > 1. [Map](https://goo.gl/maps/PuxANV1bdYuq3ja79)
> >    1. latitude = -17.8661 degrees north
> >    1. longitude = -149.6537 degrees east
> > 
> > {: .output}
> {: .solution}
{: .challenge}

{% include links.md %}