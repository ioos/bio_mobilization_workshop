# Certificates

To create certificates, run:
```bash
cd certificate/bin
python make_certificate.py
```

In `make_certificate.py` edit `config` for the persons name and date of the workshop.

This will generate `.svg` and `.pdf` certificates in the `certs/` directory. File names follow the convention `firstName_lastName_date.[svg|pdf]`



## Create the template certificate.svg

### Using Microsoft Power Point
1. Create the certificate of interest in MS Power Point.
1. Make sure to include the jinja template variables in the location you want the content to appear.
   1. For example, the appicants first name will replace the variable `{{configs.name.first_name}}` in the svg file.
1. Save the slide as SVG. File -> Save As -> select "Scalable Vector Graphics". Choose to save only the one slide.
1. This is where is gets tricky. The SVG from Power Point has some very specific formatting for text location on the slide. For example, text will be stored as `tspan` with specific x & y starting locations on the page. Unfortunately, this doesn't ensure the content is centered on the page, especially when we have variable content through the jinja template.
   ```xml
   <tspan font-family="Garamond,Garamond_MSFontService,sans-serif" font-stretch="normal" font-size="24" x="206.147" y="96">
   This certificate is awarded to
   </tspan>
    ```
   Instead, we can generalize this to a `text` element and specify center and the y location:
   ```xml
   <text font-family="Garamond,Garamond_MSFontService,sans-serif" font-stretch="normal" font-size="24" dominant-baseline="middle" text-anchor="middle" x="50%" y="270">
   This certificate is awarded to
   </text>   
   ```
1. Edit the XML in the svg file to adjust the text elements to be percentages in the x-direction. Make any other custom edits to the svg file. Note that Power Point might separate each work into it's own `tspan` element. These can be simplified into one `text` element.
1. Save the template svg as `certificate.svg` in the `templates\` directory.

### Using diagrams.net
1. Using https://app.diagrams.net/ design the certificate.
1. Include the jinja template variables where the information should be replaced.
   1. The appicants first name will replace the variable `{{configs.name.first_name}}` in the svg file.
1. Save the image as `svg`
   1. File > Export as > SVG...
   2. Set the size to `Diagram`
   3. Check `Include a copy of my diagram`
   4. Check `Embed Images`
   5. Leave `Text Settings` as `Default`
   6. Leave `Links` as `Automatic`
   7. Select `Export` and save to `certificate/bin/templates/certificate.svg`

`make_certificate.py` will pick up the template and insert the appropriate information from the `config` variable.

The variables in the svg should follow the structure of the `config` list:
```python
config = [
    {
        "name": {"first_name": "Mathew", "last_name": "Biddle"},
        "date": "2023-05-19",
    },
    {
        "name": {"first_name": "Abby", "last_name": "Benson"},
        "date": "2023-05-19",
    },
]
```

first name is accessed through `config.name.first_name`, last name through `config.name.last_name` and date is accessed through `config.date`.
