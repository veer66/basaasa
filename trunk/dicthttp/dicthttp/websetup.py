"""Setup the dicthttp application"""
import logging

from dicthttp.config.environment import load_environment

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup dicthttp here"""
    load_environment(conf.global_conf, conf.local_conf)
