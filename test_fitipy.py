import os
from os.path import isfile

from fitipy import FSet, FDict, FList


class TestFiti:
    def test_fset(self):
        obj = FSet('tmp')
        assert len(obj) == 0
        assert obj == set()
        obj.add('x')
        obj.add('x')
        assert len(obj) == 1
        assert list(obj) == ['x']
        obj2 = FSet('tmp')
        assert list(obj) == ['x']
        assert obj2 == obj
        obj.add('y')
        assert obj2 != obj
        obj2.reload()
        assert obj2 == obj
        obj.remove('x')
        str(obj)  # Ensure no exception
        repr(obj)  # Ensure no exception

    def test_fdict(self):
        obj = FDict('tmp')
        assert len(obj) == 0
        assert obj == {}
        obj['x'] = 'y'
        assert len(obj) == 1
        assert list(obj) == ['x']
        assert obj['x'] == 'y'
        obj2 = FDict('tmp')
        assert list(obj) == ['x']
        assert obj2 == obj
        obj['z'] = 'a'
        assert obj2 != obj
        obj2.reload()
        assert obj2 == obj
        del obj['z']
        str(obj)  # Ensure no exception
        repr(obj)  # Ensure no exception

    def test_flist(self):
        obj = FList('tmp')
        assert len(obj) == 0
        assert list(obj) == []
        assert obj == []
        obj.append('x')
        assert len(obj) == 1
        assert obj == ['x']
        assert obj[0] == 'x'
        obj2 = FList('tmp')
        assert obj == ['x']
        assert obj2 == obj
        obj[0] = 'a'
        assert obj2 != obj
        obj2.reload()
        assert obj2 == obj
        del obj[0]
        obj.insert(0, 'b')
        str(obj)  # Ensure no exception
        repr(obj)  # Ensure no exception

    def teardown(self):
        if isfile('tmp'):
            os.remove('tmp')
