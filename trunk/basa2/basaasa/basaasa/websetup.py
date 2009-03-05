"""Setup the basaasa application"""
import logging

from basaasa.config.environment import load_environment
from basaasa.users.authkit_elixir_driver import UsersFromDatabase
from basaasa import model
from authkit.authenticate.open_id import make_store
from pylons import config

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup basaasa here"""
    load_environment(conf.global_conf, conf.local_conf)
    from elixir import metadata    
    metadata.create_all(checkfirst=True)
    store_type = config.get('authkit.openid.store.type')
    stote_config = config.get('authkit.openid.store.config')
    conn, cstore = make_store(store_type, stote_config)
    if store_type == 'mysql':
        cstore.createTables()

