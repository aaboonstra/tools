# vim: set ts=4 sw=4 sts=4 et:
from django.utils import unittest


'''
custom assertion to check if an object exists
'''
class TestCase(unittest.TestCase):
    def get_object_or_none(model, **kwargs):
        try:
            return model.objects.get(**kwargs)
        except model.DoesNotExist:
            return None

    def expect_none(self, obj):
        if obj is not None:
            msg = '%s != \'None\'' % obj
            raise self.failureException, msg

    def expect_not_none(self, obj):
        if obj is None:
            msg = '%s == \'None\'' % obj
            raise self.failureException, msg

    assertNone = expect_none
    assertNotNone = expect_not_none 
