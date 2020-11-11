from flask import flash

__all__ = ['FlaskInform', 'Attention']

class Attention:
    danger = 'danger'
    success = 'success'
    warning = 'warning'

class FlaskInformMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['message'] = attrs['m'] = attrs['__annotations__']['m']
        attrs['l'] = attrs['__annotations__'].get('l', Attention.danger)
        del attrs['__annotations__']
        return super().__new__(cls, name, bases, attrs)

class FlaskInform(Exception, metaclass=FlaskInformMeta):
    m: ''

    def __str__(self):
        return self.message

    def __repr__(self):
        return f'{self.__class__.__name__}()'

    @classmethod
    def flash(cls, suppl=None):
        if suppl:
            flash(f'{cls.m}: {suppl}', cls.l)
        else:
            flash(cls.m, cls.l)