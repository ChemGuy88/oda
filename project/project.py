#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    Project
'''

import csv, json, re, requests, string, sys
import gudhi as gd
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import pandas as pd
import scipy as sp
import scipy.spatial as spt
import seaborn as sns
from sklearn import manifold

corr_protein = pd. read_csv("mypath/1anf.corr_1.txt",
                            header=None,
                            delim_whitespace=True )
dist_protein_1 = 1 - np.abs( corr_protein_1.values )
rips_complex_1 = gd.RipsComplex(distance_matrix=dist_protein_1, max_edge_length =1.1)
simplex_tree_1 = rips_complex_1.create_simplex_tree(max_dimension=2)

interv0_1 = simplex_tree_1.persistence_intervals_in_dimension(0)
interv0_2 = simplex_tree_2.persistence_intervals_in_dimension(0)
bot0 = gd.bottleneck_distance( interv0_1, interv0_2 )
interv1_1 = simplex_tree_1.persistence_intervals_in_dimension(1)
interv1_2 = simplex_tree_2.persistence_intervals_in_dimension(1)
bot1 = gd.bottleneck_distance( interv1_1 , interv1_2 )

mds = manifold .MDS(n_components=2, dissimilarity="precomputed")
config = mds.fit(M).embedding_
plt.scatter(config [0:7,0], config [0:7, 1], color='red', label="closed")
plt.scatter(config [7:l,0], config [7:l, 1], color='blue', label="red")
plt.legend(loc = 1)
