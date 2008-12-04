import dictclient

def simplify_def(define):
    return {"def": define.getdefstr(),
            "word": define.getword(),
            "database": define.getdb().getname()}

class DictClientError(RuntimeError):
    pass

class DictClientWrapper:
    def __init__(self, server='localhost', port=2628):
        self.conn = dictclient.Connection(server, port)

    def define(self, word, database='*'):
        try:
            def_list = self.conn.define(word=word, database=database)
        except Exception, e:
            raise DictClientError(str(e))
        return map(simplify_def, def_list)

    def match(self, word, database='*', strategy="word"):
        try:
            def_list = self.conn.match(word=word, 
                                       database=database,
                                       strategy=strategy)
        except Exception, e:
            raise DictClientError(str(e))
        return map(simplify_def, def_list)


    def strategies(self):
        return self.conn.getstratdescs().keys()

    def databases(self):
        if not hasattr(self.conn, 'dbobjs'):
            raise DictClientError('database object is not available')
        db = {}
        for dbname in self.conn.dbobjs:
            source = self.conn.dbobjs[dbname]
            db[dbname] = {"name": source.getname(),
                          "desc": source.getdescription(),
                          "info": source.getinfo()}
        return db

    def close(self):
        self.conn.sock.close()

if __name__ == '__main__':
    wrapper = DictClientWrapper("dict.org")
    print wrapper.define("dick")
    print
    print
    print "----"
    print
    print wrapper.strategies()
    print
    print wrapper.match("dick")
    print
    print
    print wrapper.databases()
