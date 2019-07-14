#!/usr/bin/env python3
import argparse
import os
import re
import sys
import webbrowser
from importlib import import_module

from iterfzf import iterfzf


def main():
    parser = argparse.ArgumentParser(description='doc-fzf.')
    parser.add_argument('module_name',
                        type=str,
                        help='Name of the module to search')
    parser.add_argument('-q',
                        dest="query",
                        type=str,
                        default=None,
                        help='Query the docs')
    args = parser.parse_args()

    if args.module_name.lower() == "ansible":
        from doc_fzf.modules.ansible import Scrapper
    elif args.module_name.lower() == "python":
        from doc_fzf.modules.python import Scrapper
    else:
        print("Dynamic modules not yet supported")
        sys.exit(2)

    dynamic_fzf = Scrapper()

    # To get a clean list to be displayed by FZF we want to display only the
    # description of the documentation but we want to preserve the URL in memory
    # to return it to our web browser.
    urls = []
    descriptions = []
    try:
        for doc in dynamic_fzf.get_documentation():
            urls.append(doc[0])
            descriptions.append(doc[1])
    except Exception as error:
        raise(error)
        sys.exit(2)

    if args.query:
        # Allow the user to start FZF with a query
        url = iterfzf(descriptions, exact=True, query=args.query)
    else:
        # Otherwise, just give all the results
        url = iterfzf(descriptions, exact=True)

    # Is there a better way to do this?
    for u, d in zip(urls, descriptions):
        if url == d:
            try:
                # Open URL in a new tab
                webbrowser.open(u, new=2)
                print(u)
            except Exception as error:
                # If webbrowser cannot open the URL just print it.
                print(u)


if __name__ == "__main__":
    main()
