import os
from xossynchronizer import Synchronizer
from xosconfig import Config

base_config_file = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + '/config.yaml')
mounted_config_file = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + '/mounted_config.yaml')

if os.path.isfile(mounted_config_file):
    Config.init(base_config_file, 'synchronizer-config-schema.yaml', mounted_config_file)
else:
    Config.init(base_config_file, 'synchronizer-config-schema.yaml')

Synchronizer().run()
