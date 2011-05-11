# -*- coding: utf-8 -*-
import collections


class InvalidOperatorError(ValueError): pass
class DuplicateFieldError(ValueError): pass


class FieldDict(dict):
    def __setitem__(self, k, v):
        if k in self:
            raise DuplicateFieldError('Field "{0}" already set.'.format(k))

        super(FieldDict, self).__setitem__(k, v)


    def update(self, e, **f):
        raise NotImplementedError()



class OperatorDict(collections.defaultdict):
    OPERATORS = ('$inc', '$rename')

    def __init__(self):
        super(OperatorDict, self).__init__(FieldDict)


    def __setitem__(self, k, v):
        if k not in self.OPERATORS:
            raise InvalidOperatorError('"{0}" is not a valid operator'.format(k))

        super(OperatorDict, self).__setitem__(k, v)


    def update(self, e, **f):
        raise NotImplementedError()


class Update(object):
    def __init__(self):
        self._ops = OperatorDict()


    def __iter__(self):
        return self._ops.iteritems()


    def inc(self, field, increment):
        """
        >>> update = Update()
        >>> update.inc('foo', 'bar')
        >>> dict(update)
        {'$inc': {'foo': 'bar'}}
        """
        self._ops['$inc'][field] = increment


    def rename(self, old, new):
        """
        >>> update = Update()
        >>> update.rename('old', 'new')
        >>> dict(update)
        {'$rename': {'old': 'new'}}
        """
        self._ops['$rename'][old] = new
