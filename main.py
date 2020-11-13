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
        attrs['d'] = attrs['__annotations__'].get('d', ': ')
        del attrs['__annotations__']
        return super().__new__(cls, name, bases, attrs)

class FlaskInform(Exception, metaclass=FlaskInformMeta):
    """Subclass this class and define:
        m: message,
        l: level (optional, default = 'danger'),
        d: delimiter (optional, default = ': '),
    """

    m: ''

    def __str__(self):
        return self.message

    def __repr__(self):
        return f'{self.__class__.__name__}()'

    @classmethod
    def flash(cls, suppl=None):
        if suppl:
            flash(f'{cls.m}{cls.d}{suppl}', cls.l)
        else:
            flash(cls.m, cls.l)