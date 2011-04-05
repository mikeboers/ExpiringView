ExpiringView
=============

A wrapper around a mapping which allows for key/value pairs to expire. Wrap this around a `shelve.Shelve` for a quick and dirty cache.

Note that pairs only expire when accessed, so to purge all old data one must iterate across the entire wrapper.

Please see docstrings for more extensive documentation.
