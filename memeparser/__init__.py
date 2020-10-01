__version__ = '0.1.0'

import numpy as np
import glob
import os
class MemeParser:
    def __init__(self, fpath):
        self.fpath = fpath
        self.values = []
        with open(fpath) as f:
            self.lines = [x.rstrip("\n") for x in f.readlines()]
        for line in self.lines:
            if line.startswith("MEME version "):
                self.version = int(line.replace("MEME version ", ""))
            elif line.startswith("ALPHABET="):
                self.alphabet = [x for x in line.replace("ALPHABET= ", "")]
            elif line.startswith("strands: "):
                self.strands = line.replace("strands: ", "").split(" ")
            elif line.startswith("A "):
                l = line.split(" ")
                letters = l[::2]
                nums = [float(x) for x in l[1::2]]
                self.background_letter_frequencies = \
                    {key: val for key, val in zip(letters, nums)}
            elif line.startswith("MOTIF "):
                self.id, self.name = line.replace("MOTIF ", "").split(" ")
            elif line.startswith("letter-probability matrix: "):
                s = line.replace("letter-probability matrix: ", "").replace("= ", ":::")
                pairs = s.split(" ")
                self.alength, self.w, self.nsites, self.E = \
                     [int(x.split(":::")[1]) for x in pairs]
            elif line.startswith(" "):
                self.values.append([float(x) for x in line.strip().split("  ")])
            elif line.startswith("URL "):
                self.url = line.replace("URL ", "")
                self.values = np.array(self.values)
    
    def __iter__(self):
        self.iter_idx = 0
        return self
    
    def __next__(self):
        if self.iter_idx < self.w:
            result = self.values[self.iter_idx]
            self.iter_idx += 1
            return result
        else:
            raise StopIteration
        

# the url however does not lead to plain text
# the properties are all properties not beginning with "__"
# iterator iterates over self.values.
