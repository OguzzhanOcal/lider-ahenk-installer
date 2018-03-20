#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import yaml, os, io, json

class ConfigManager(object):

    """
    method reading from the configuration file /conf/lider-ahenk.yml
    """

    def __init__(self):
        self.conf_file_path = os.path.join( os.path.dirname( os.path.abspath( __file__ ) ),'../../conf/lider-ahenk.yml' )

    def read(self):
        with open(self.conf_file_path, 'r') as stream:

            try:
                return yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                return None
