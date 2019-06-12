import os


class PairFile:
    def is_existed(self, pair_file):
        # global pair_file
        for single in pair_file:
            if self.path == single.path:
                return 4
            elif self.keyword == single.keyword:
                return 5

    def __call__(self, path, keyword):
        self.__init__(path, keyword)

    def __init__(self, path, keyword, index=None):
        self.path = path
        self.name = os.path.basename(path)
        self.keyword = keyword
        self.index = index
