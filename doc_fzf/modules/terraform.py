""" Terraform doc-fzf module

This module will query https://www.terraform.io/docs/providers/aws/index.html
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
        self.base_url = "https://www.terraform.io"
        self.documentation_url = "{0}/docs/providers/aws/index.html".format(self.base_url)
        FZFDoc.__init__(self, self.documentation_url)

    def get_documentation(self):
        """ Return a tuple of (url, description)
        """
        soup = BeautifulSoup(self.load_html(), "html.parser")
        for l in soup.select("ul.nav.docs-sidenav > li > ul > li"):
            for li in l.findAll('a'):
                href = li.get('href')
                suffix = ''
                if href.startswith('/docs/providers/aws/r/'):
                    suffix = '(resource)'
                elif href.startswith('/docs/providers/aws/d/'):
                    suffix = '(data)'
                elif href.startswith('/docs/providers/aws/guides/'):
                    suffix = '(guide)'
                else:
                    suffix = '(other)'
                yield ("{0}{1}".format(self.base_url, href), "{0} {1}".format(li.getText(), suffix))
