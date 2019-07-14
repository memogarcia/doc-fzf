""" Ansible doc-fzf module

This module will query https://docs.ansible.com/ansible/latest/modules/list_of_all_modules.html
to get a list of (url, description)

Is implemented using requests and bs4 but you can use any other tools you like.

Any module implemented by doc-fzf must inherit `from pyfzf import FZFDoc`
and implement a `get_documentation()` function

FZFDoc base class will handle the cache layer for you!!
"""

import requests
from bs4 import BeautifulSoup

from doc_fzf.pyfzf import FZFDoc


class Scrapper(FZFDoc):
    def __init__(self):
        self.base_url = "https://docs.ansible.com/ansible/latest/modules"
        self.documentation_url = "{0}/list_of_all_modules.html".format(self.base_url)
        FZFDoc.__init__(self, self.documentation_url)

    def get_documentation(self):
        """ Return a tuple of (url, description)
        """
        soup = BeautifulSoup(self.load_html(), "html.parser")
        for l in soup.findAll("ul", {"class": "simple"}):
            for li in l.findAll('li'):
                for lii in li.findAll('a'):
                    href = lii.get('href')
                    yield ("{0}/{1}".format(self.base_url, href), "{0}".format(li.getText()))
