"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import orm

from basaasa.model import meta
import elixir  

sm = orm.sessionmaker(autoflush=True, autocommit=True)  
elixir.session = orm.scoped_session(sm) 
meta.Session = elixir.session
elixir.options_defaults.update({'shortnames': True})

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    ## Reflected tables must be defined and mapped here
    #global reflected_table
    #reflected_table = sa.Table("Reflected", meta.metadata, autoload=True,
    #                           autoload_with=engine)
    #orm.mapper(Reflected, reflected_table)

    elixir.metadata.bind = engine
    meta.engine = engine


## Non-reflected tables may be defined and mapped at module level
#foo_table = sa.Table("Foo", meta.metadata,
#    sa.Column("id", sa.types.Integer, primary_key=True),
#    sa.Column("bar", sa.types.String(255), nullable=False),
#    )
#
#class Foo(object):
#    pass
#
#orm.mapper(Foo, foo_table)


## Classes for reflected tables may be defined here, but the table and
## mapping itself must be done in the init_model function
#reflected_table = None
#
#class Reflected(object):
#    pass

from elixir import *

elixir.setup_all()
