'''
This file is unfinnished. POTENTIAL OF REMOVAL
'''
import numpy as np;

from combinator import Combinator;
from edge import Edge;
#from sampler import Sampler;
from dataTransformer import DataTransformer
from node import Node;

class MATRCS:
    def __init__(self, slp, dims=0, M=2):
        self.slope_ = slp;
        #self.sampler = Sampler();
        self.Transformer = DataTransformer(True);
        self.terms = {0: 1, 1: 2, 2: 3, 3: 1, 4: 1, 5: 1, 6: 4, 7: 1, 8: 1}
        self.F = 9;
        self.V = dims;
        self.M = M;
        print("Max interactions set to degree ", self.M);

