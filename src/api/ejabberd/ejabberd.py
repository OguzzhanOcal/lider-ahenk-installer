#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: İsmail BAŞARAN <ismail.basaran@tubitak.gov.tr> <basaran.ismaill@gmail.com>
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import yaml, os, io, json

class EjabberInstaller(object):

    def __init__(self, ssh_api):
        self.ssh_api = ssh_api
        self.jabberd_template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../conf/ejabberd_temp.yml')
        self.jabberd_out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist/ejabberd.yml')
        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist')):
            os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../dist'))
        self.cmd_install = "echo 1 | sudo -S apt -y install ejabberd"


    def read_temp_yml_file(self):
        with open(self.jabberd_template_path , 'r') as stream:
            try:
                return yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                return None

    def write_to_yml(self,data):
        with io.open(self.jabberd_out_path, 'w', encoding='utf8') as outfile:
            yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)
    
    def install(self, data):
        yml_data = self.read_temp_yml_file()
        #json_data = json.load(yml_data)
        #yml_data['hosts'] = ['localhost','192.168.1.1']
        for attr in data:
            yml_data[attr] = data[attr]
        self.write_to_yml(yml_data)
        self.ssh_api.run_command(self.cmd_install)