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
from elixir.ext.versioned import acts_as_versioned

class User(Entity):
    uid = Field(Integer, primary_key=True)
    username = Field(String(255), unique=True, nullable=False)
    password = Field(String(255), nullable=False)
    group = ManyToOne("Group")
    roles = ManyToMany("Role", lazy=True) 
    group = ManyToOne("Group") 

    def __init__(
        self,
        username,
        uid=None,
        password=None,
        group_uid=None,
    ):
        Entity.__init__(self)
        self.uid        = uid
        self.username   = username
        self.password   = password
        self.group_uid  = group_uid
        
    def __repr__(self):
        return "User(%(username)s)" % self.__dict__

class Group(Entity):
    uid = Field(Integer, primary_key=True)
    name = Field(String(255), unique=True, nullable=False)
    users = OneToMany("User")

    def __init__(self, name=None):
        Entity.__init__(self)
        self.name = name
        
        def __repr__(self):
            return "Group(%(name)s)" % self.__dict__
        
class Role(Entity):
    uid = Field(Integer, primary_key=True)
    name = Field(String(255), unique=True, nullable=False)
    users = ManyToMany("User", lazy=True) 

    def __init__(self, name=None):
        Entity.__init__(self)
        self.name = name
    
    def __repr__(self):
        return "Role(%(name)s)" % self.__dict__

class Document(Entity):
    body = Field(Unicode, nullable=False)
    title = Field(Unicode(255))
    checking_needed = Field(Boolean, default=False, nullable=False)
    latest_editor = ManyToOne("User")
    acts_as_versioned()

class Comment(Entity):
    body = Field(Unicode)
    author = ManyToOne("User")
    document = ManyToOne("Document")
    
class Translation(Entity):
    body = Field(Unicode)
    title = Field(Unicode(255))
    latest_editor = ManyToOne("User")
    document = ManyToOne("Document")
    acts_as_versioned()
    
class Dictionary(Entity):
    name = Field(Unicode(255), unique=True, nullable=False)
    entries = OneToMany("DictEntry")
    
class DictEntry(Entity):
    data = Field(Unicode)
    dictionary = ManyToOne("Dictionary")
    keys = OneToMany("DictKey")
    
class DictKey(Entity):
    keyword = Field(Unicode(255))
    type = Field(String)
    entry = ManyToOne("DictEntry")
    
elixir.setup_all()