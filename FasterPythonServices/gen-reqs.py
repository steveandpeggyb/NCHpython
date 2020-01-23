#!/usr/bin/env python

import yaml

with open('environment.yml') as fp:
    env = yaml.load(fp)

with open('requirements.txt', 'wt') as out:
    for dep in env['dependencies']:
        # conda-forge::python-levenshtein=0.12.0
        i = dep.find('::')
        if i != -1:
            dep = dep[i+2:]
        dep = dep.replace('=', '==')
        dep = dep.replace('redis-py', 'redis')
        print(dep, file=out)
