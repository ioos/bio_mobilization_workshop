# Certificates for The Carpentries

To create the certificate, run:
```bash
python make_certificate.py
```

In `make_certificate.py` edit `config` for the persons name and date of the workshop.


## Create the template certificate.svg

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

The variables in the svg should follow the structure of the `config` dictionary:
```python
config = {
    "name": {"first_name": "Mathew", "last_name": "Biddle"},
    "date": "2023-05-19",
}
```

first name is accessed through `config.name.first_name`, last name through `config.name.last_name` and date is accessed through `config.date`.

## Historical information:

There are two ways to build certificates from this repo, one depends on the python package cairosvg which in turn depends on cairo development libraries being installed. To use this method, use `bin/certificates.py` to build certificates.

The second, pure python method uses the python packages jinja2, jinja2-cli and svglib to build the certificates.

To build certificates this way, you can run:
```
jinja2 swc-attendance.svg -D name="Firstname Lastname" -D date="Nov. 6, 2017" -D instructor="Some Instructor Name" > lastname_firstname.svg
svg2pdf lastname_firstname.svg 
```
