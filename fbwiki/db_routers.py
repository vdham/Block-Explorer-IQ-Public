
class mainRouter(object):
    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def db_for_read(self, model, **hints):
        return 'readonly'
