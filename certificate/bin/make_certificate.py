import os
from jinja2 import Environment, FileSystemLoader
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF


def svg2pdf(fname):
    drawing = svg2rlg(fname)
    outname = fname.replace(".svg", ".pdf")
    renderPDF.drawToFile(drawing, outname)


def write_svg_cert(template, config):
    root = os.path.dirname(os.path.abspath(__file__))
    # root = path to output directory
    fname = (
        config["name"]["first_name"]
        + "_"
        + config["name"]["last_name"]
        + "_"
        + config["date"]
        + ".svg"
    )
    filename = os.path.join(root, "certs", fname)
    with open(filename, "w") as fh:
        fh.write(template.render(configs=config))

    svg2pdf(filename)


def load_template():
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, "templates")
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template("certificate.svg")
    return template


def write_templates(config):
    # filename = parse_args()
    template = load_template()
    write_svg_cert(template, config)


def main(config):
    for person in config:
        write_templates(person)


if __name__ == "__main__":
    config = [
        {
            "name": {"first_name": "Abby", "last_name": "Benson"},
            "date": "2023-05-19",
        },
        {
            "name": {"first_name": "Matt", "last_name": "Biddle"},
            "date": "2023-05-19",
        },
        {
            "name": {"first_name": "Julieta", "last_name": "Maldonado"},
            "date": "2023-05-19",
        },
        {
            "name": {"first_name": "Errol", "last_name": "Ronje"},
            "date": "2023-05-19",
        },
        {
            "name": {"first_name": "Kylie", "last_name": "Langlois"},
            "date": "2023-05-19",
        },
        {
            "name": {"first_name": "Laura", "last_name": "Teed"},
            "date": "2023-05-19",
        },
        {
            "name": {"first_name": "Kourtney", "last_name": "Burger"},
            "date": "2023-05-19",
        },
        {
            "name": {"first_name": "Javier", "last_name": ""},
            "date": "2023-05-19",
        },
        {
            "name": {"first_name": "Fernando García", "last_name": "González"},
            "date": "2023-05-19",
        },
        {
            "name": {"first_name": "Marine", "last_name": "Lebrec"},
            "date": "2023-05-19",
        },
        {
            "name": {"first_name": "Marc", "last_name": "Ghergariu"},
            "date": "2023-05-19",
        },
        {
            "name": {"first_name": "Rodrigo J.", "last_name": "Gonçalves"},
            "date": "2023-05-19",
        },
    ]

    main(config)
