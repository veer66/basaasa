"""Setup the basaasa application"""
import logging

from basaasa.config.environment import load_environment

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup basaasa here"""
    load_environment(conf.global_conf, conf.local_conf)
    from elixir import metadata
    metadata.create_all(checkfirst=True)
