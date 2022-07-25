import json
import logging


oLogger = logging.getLogger(__name__)

config_path = './webapp/cds_hooks/config/cds-hooks.config.json'
with open(config_path, 'r') as oFile:
    json_string = oFile.read()
    oLogger.debug(config_path)

config = json.loads(json_string)
