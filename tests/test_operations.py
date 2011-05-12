# -*- coding: utf-8 -*-
import dibble.model

class TestModel(dibble.model.Model):
    counter = dibble.fields.Field(default=1)


def test_set():
    m = TestModel()
    m.counter.set(2)

    assert dict(m.update) == {'$set': {'counter': 2}}
    assert m.counter.value == 2


def test_increment():
    m = TestModel()
    m.counter.inc(1)

    assert dict(m.update) == {'$inc': {'counter': 1}}
    assert m.counter.value == 2
