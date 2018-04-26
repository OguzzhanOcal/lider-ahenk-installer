#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import sys, yaml, os, io
from ruamel.yaml import YAML


class ConfigManager(object):

    """
    method reading and writing from the configuration file
    """

    def __init__(self):
        self.yaml = YAML()
        self.yaml.indent(mapping=4)
        self.installer_config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../conf/installer_config.yml' )
        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist')):
            os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist'))

    def read(self):
        with open(self.installer_config_path, 'r') as stream:
            try:
                return yaml.load(stream)
                # return self.yaml.load(stream)
            except Exception as exc:
                print(exc)
                return None

    def read_temp_yml_file(self, path):
        with open(path, 'r') as stream:
            try:
                return self.yaml.load(stream)
            except Exception as exc:
                print(exc)
                return None

    def write_to_yml(self, data, path):
        with io.open(path, 'w', encoding='utf8') as outfile:
            #self.yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)
            self.yaml.dump( data, outfile)

    def replace_all(self, text, dic):
        for i, j in dic.items():
            text = text.replace(i, j)
        return text
