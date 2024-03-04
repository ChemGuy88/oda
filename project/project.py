#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Project tutorial

https://github.com/GUDHI/TDA-tutorial/blob/master/Tuto-GUDHI-persistence-diagrams.ipynb
'''

'''#####################################################################
###### Universal Variables #############################################
########################################################################'''

import sys
from pathlib import Path

userDir = str(Path.home())
workDir = f'{userDir}/Documents/oda/project'
dataDir = f'{workDir}/data/corr/0_mbp_closed'

plt.close()

'''
Their code
'''

import gudhi as gd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
import scipy.spatial as spt
import seaborn as sns
from sklearn import manifold

'''### Compute persistence diagrams ############################################################'''

corr_protein_1 = pd. read_csv(f'{dataDir}/1anf.corr_1.txt',
                            header=None,
                            delim_whitespace=True )
# corr_protein_1.head()
dist_protein_1 = 1 - np.abs( corr_protein_1.values )
rips_complex_1 = gd.RipsComplex(distance_matrix=dist_protein_1, max_edge_length =1.1)
simplex_tree_1 = rips_complex_1.create_simplex_tree(max_dimension=2)
diag_1 = simplex_tree_1.persistence()
gd.plot_persistence_diagram(diag_1)

# Inferred code
if True:
    simplex_tree_2 = rips_complex_1.create_simplex_tree(max_dimension=2)
    diag_2 = simplex_tree_2.persistence()
    gd.plot_persistence_diagram(diag_2)

'''### Compare persistence diagrams using bottleneck distance ###############'''
if False:
    # 0-homologies
    interv0_1 = simplex_tree_1.persistence_intervals_in_dimension(0)
    interv0_2 = simplex_tree_2.persistence_intervals_in_dimension(0)
    bot0 = gd.bottleneck_distance( interv0_1, interv0_2 )
    # 1-homologies
    interv1_1 = simplex_tree_1.persistence_intervals_in_dimension(1)
    interv1_2 = simplex_tree_2.persistence_intervals_in_dimension(1)
    bot1 = gd.bottleneck_distance( interv1_1 , interv1_2 )

    mds = manifold.MDS( n_components=2, dissimilarity="precomputed")
    config = mds.fit(dist_protein_1).embedding_

    plt.scatter( config[0:7, 0], config[0:7, 1], color='red', label='closed')
    plt.scatter( config[1:7, 0], config[7:1, 1], color='blue', label='red')
    plt.legend(loc=1)
