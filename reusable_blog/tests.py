# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from .models import Post

class PostTest(TestCase):
    """
    Here we'll define the tests
    that we'll run against our Post model
    """

    def test_str(self):
        test_title = Post(title='My Latest Blog Post')
        self.assertEqual(str(test_title),'My Latest Blog Post')