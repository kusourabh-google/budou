# -*- coding: utf-8 -*-
#
# Copyright 2016 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import os
import budou

class TestStandardCacheFactory(unittest.TestCase):

  def setUp(self):
    self.cache = budou.load_cache()

  def tearDown(self):
    if os.path.isfile(self.cache.DEFAULT_FILE_PATH):
      os.remove(self.cache.DEFAULT_FILE_PATH)
    self.cache = None

  def test_load(self):
    cache_type = repr(self.cache)
    self.assertEqual('<ShelveCache>', cache_type,
        'ShelveCache should be loaded under standard environment.')

  def test_set_and_get(self):
    source = 'apple'
    language = 'a'
    target = 'banana'
    self.cache.set(source, language, target)


    # Removing this test because shelve module can put a different extra suffix
    # by low-level library.
    # TODO (tushuhei) Update the cache mechanism to use pickle instead.
    #self.assertTrue(os.path.isfile(self.cache.DEFAULT_FILE_PATH),
    #    'Cache file should be generated.')
    self.assertEqual(self.cache.get(source, language), target,
        'The target should be cached.')

  def test_cache_key(self):
    self.cache.set('a', 'en', 1)
    self.cache.set('a', 'ja', 2)
    self.cache.set('b', 'en', 3)
    self.assertNotEqual(
        self.cache.get('a', 'en'), self.cache.get('b', 'en'),
        'The cached key should be unique per source text.')
    self.assertNotEqual(
        self.cache.get('a', 'en'), self.cache.get('a', 'ja'),
        'The cached key should be unique per language.')

if __name__ == '__main__':
  unittest.main()

