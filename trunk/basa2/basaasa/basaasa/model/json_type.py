# Copyright (C) 2005, 2006, 2007, 2008 Michael Bayer mike_mp@zzzcomputing.com
#
# This module is part of SQLAlchemy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

from sqlalchemy.types import MutableType, TypeDecorator, Binary
from simplejson import loads, dumps 

class JsonType(MutableType, TypeDecorator):
    impl = Binary
    
    def __init__(self, mutable=True, comparator=None):
        self.mutable = mutable
        self.comparator = comparator
        super(JsonType, self).__init__()

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        return dumps(value)

    def process_result_value(self, value, dialect):        
        if value is None:
            return None
        return loads(str(value))

    def copy_value(self, value):
        if self.mutable:
            return loads(dumps(value))
        else:
            return value

    def compare_values(self, x, y):
        if self.comparator:
            return self.comparator(x, y)
        elif self.mutable:
            return dumps(x) == dumps(y)
        else:
            return x == y

    def is_mutable(self):
        return self.mutable