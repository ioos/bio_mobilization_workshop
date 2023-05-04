from jinja2 import Environment, FileSystemLoader
# import argparse
import json
import os
import shutil
import sys

def write_svg_cert(template, config):
    root = os.path.dirname(os.path.abspath(__file__))
    #root = path to output directory
    fname = config['name']['first_name']+'_'+config['name']['last_name']+'_'+config['date']+'.svg'
    filename = os.path.join(root, 'certs', fname)
    with open(filename, 'w') as fh:
        fh.write(template.render(configs = config))
def load_template():
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'templates')
    env = Environment( loader = FileSystemLoader(templates_dir) )
    template = env.get_template('cert_template.svg')
    return template

def write_templates(config):
    # filename = parse_args()
    template = load_template()
    write_svg_cert(template, config)

def main(config):
    write_templates(config)


if __name__ == '__main__':

    config = {'name': {'first_name': 'matt',
                       'last_name' : 'biddle'},
              'date': '2023-05-19',
              }

    main(config)