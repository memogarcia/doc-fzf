# Doc-FZF: Modular CLI Documentation Fuzzy Finder

Fuzzy Search documentation from the CLI

**Disclaimer** This tool was built to learn `FZF` capabilities. Feel free to use it or extend it.

## Usage

    doc-fzf ansible
    doc-fzf ansible -q yum

## Installation

    pip3 install doc-fzf

Verify your installation:

    doc-fzf -h

```bash
usage: doc-fzf.py [-h] [-q QUERY] module_name

doc-fzf.

positional arguments:
  module_name  Name of the module to search

optional arguments:
  -h, --help   show this help message and exit
  -q QUERY     Query the docs
```

## Extending Doc-FZF

`doc-fzf` is a modular application, it can load modules at runtime that scrap websites in any way you like.

Any module should always contain:

* class name must always be `Screapper(FZFDoc)`
* `self.documentation_url` attribute
* `def get_documentation(self):` function that will return a tuple ("url", "description")

```python
from doc_fzf.pyfzf import FZFDoc


class Scrapper(FZFDoc):
    def __init__(self):
        self.base_url = "https://docs.python.org/3"
        self.documentation_url = "{0}/py-modindex.html".format(self.base_url)
        FZFDoc.__init__(self, self.documentation_url)

    def get_documentation(self):
        """ Return a tuple of (url, description)
        """
        Doc = namedtuple('Doc', ['url', 'description'])
        example_doc = [Doc("url", "description")]
        for doc in example_doc:
            yield (doc.url, doc.description)
```

## References

* [Doc-FZF: Modular CLI Documentation Fuzzy Finder](https://gitlab.com/memogarcia/doc-fzf)
* [fzf, A command-line fuzzy finder](https://github.com/junegunn/fzf)
* [iterfzf, Pythonic interface to fzf, a CLI fuzzy finder](https://github.com/dahlia/iterfzf)
