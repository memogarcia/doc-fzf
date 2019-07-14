"""
This module contains the base class from which modules will inhertit
"""

import os

import requests

from doc_fzf.cache import FSCache


class FZFDoc:
    """ Base class for doc-fzf modules """

    def __init__(self, documentation_url):
        self.documentation_url = documentation_url

    def load_html(self):
        """ Return an HTML string from a URL.

        HTML will be retreived from cache, if not found, it will fetch the page
        with a GET request, put it in cache and return the content
        """
        cache = FSCache()
        cached_content = cache.get(self.documentation_url)

        if cached_content:
            return cached_content
        else:
            page = requests.get(self.documentation_url)
            cache.add(self.documentation_url, str(page.content))
            return page.content

    def get_documentation(self):
        """ All module instances must implement this function.

        This function allows you to scrap your documentation website in any way you like,
        but always returning a tuple of (url, description)
        """
        raise NotImplementedError(
            "get_documentation() not implemented for this module")
