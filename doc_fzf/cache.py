import hashlib
import os


def to_hash(string):
    """ Hash a string, in this case a url.

    :param str: a str containing an url
    :return str: a sha256 hashed string
    """
    hash_object = hashlib.sha256(bytes(string.encode("utf-8")))
    return hash_object.hexdigest()


class FSCache:
    """ File System KV cache for URLs.
    It exposes the following methods:

    add(url, content)

    get(url)

    delete(url)

    delete_all()
    """
    def __init__(self):
        self.cache_dir = "/tmp/doc-fzf"
        self.create_cache_dir()

    def create_cache_dir(self):
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def add(self, key, value):
        hashed_key = to_hash(key)
        with open("{0}/{1}.html".format(self.cache_dir, hashed_key), "w", encoding='utf8') as fd:
            # TODO: fix this
            value = value.replace("\\xe2\\x80\\x93", "-")
            fd.write("{0} {1}".format(key, value))

    def get(self, key):
        hashed_key = to_hash(key)
        if os.path.isfile("{0}/{1}.html".format(self.cache_dir, hashed_key)):
            return open("{0}/{1}.html".format(self.cache_dir, hashed_key), "r", encoding='utf8')
        else:
            return None

    def delete(self, key):
        hashed_key = to_hash(key)
        try:
            os.remove("{0}/{1}.html".format(self.cache_dir, hashed_key))
        except OSError as error:
            print(error)

    def delete_all(self):
        files = [f for f in os.listdir(self.cache_dir) if f.endswith(".html")]
        for f in files:
            try:
                os.remove(os.path.join(self.cache_dir, f))
            except OSError as error:
                print(error)
