"""Setup the basaasa application"""
import logging

from basaasa.config.environment import load_environment
from basaasa.users.authkit_elixir_driver import UsersFromDatabase
from basaasa import model

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup basaasa here"""
    load_environment(conf.global_conf, conf.local_conf)
    from elixir import metadata
    users = UsersFromDatabase(model)
    metadata.create_all(checkfirst=True)
    users.user_create("admin", password="password")
