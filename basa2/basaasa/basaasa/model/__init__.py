"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import orm

from basaasa.model import meta
import elixir
from json_type import JsonType  

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
from ext import acts_as_versioned

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

from basaasa.users import edit_distance

class Document(Entity):
    body = Field(Unicode(10000000), nullable=False)
    segment = Field(JsonType)
    title = Field(Unicode(255))
    checking_needed = Field(Boolean, default=False, nullable=False)
    latest_editor = ManyToOne("User")
    lazy_deleted = Field(Boolean, default=False, nullable=False)
    translations = OneToMany("Translation", order_by="-id")
    lang = Field(Unicode(255))
    acts_as_versioned()
    
    def lazy_delete(self):
        self.lazy_deleted = True
        
    def get_version_with_editor(self, version_no):
        version = self.get_version(version_no)
        user = User.get(version.latest_editor_uid)
        version.latest_editor = user
        return version
        
    @staticmethod
    def list():
        return Document.query.filter_by(lazy_deleted=False).all()
    
    def latest_translation(self):
        if self.is_exist_translation():
            return self.translations[0]
        else:
            return None
            
    def is_exist_translation(self):
        return (len(self.translations) != 0)
    
    def textunits(self):
        return self.body.split("|")

    def get_similar_fragments(self, fragment):
        # this method will be language specific
        # search all in the corpus?
        translations = self.translations
        if len(translations) < 1:
            return []
        translation = translations[0].body.split("\n")
        fragment = map(lambda s: s.lower(), fragment.split(" "))
        ans = []
        for i, s in enumerate(self.segment.split("\n")):
            s = map(lambda s: s.lower(), s.split(" "))
            d = edit_distance(fragment, s)
            diff = max(float(d) / float(len(fragment)), float(d) / float(len(s)))            
            if diff < 0.3:
                ans.append((" ".join(s), translation[i], 1.0 - diff))
        return ans    
    
class Comment(Entity):
    body = Field(Unicode(1000000))
    author = ManyToOne("User")
    document = ManyToOne("Document")
    
class Translation(Entity):    
    title = Field(Unicode(255))
    body = Field(JsonType)
    lang = Field(Unicode(255))
    source_version = Field(Integer)
    latest_editor = ManyToOne("User")
    document = ManyToOne("Document")
    acts_as_versioned()
    
class Dictionary(Entity):
    name = Field(Unicode(255), unique=True, nullable=False)
    entries = OneToMany("DictEntry")
    
class DictEntry(Entity):
    data = Field(Unicode(1000000))
    dictionary = ManyToOne("Dictionary")
    keys = OneToMany("DictKey")
    
class DictKey(Entity):
    keyword = Field(Unicode(255))
    type = Field(String(100))
    entry = ManyToOne("DictEntry")
    
class Service(Entity):
    name = Field(Unicode(255))
    type = Field(Unicode(255))
    url = Field(Unicode(4096))
    
class UserDict(Entity):
    owner = ManyToOne("User")
    lang = Field(Unicode(64))
    headword = Field(Unicode(255))
    data = Field(JsonType)
    
    def translations(self, translations=None):
        if translations is None:
            return self.data
        else:
            self.data = translations
        
elixir.setup_all()