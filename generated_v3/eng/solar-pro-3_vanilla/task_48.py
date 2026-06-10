#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ASE script to compute interatomic distances between atom 0 and all other atoms of a Cu FCC bulk 2x2x2 supercell.
Periodic boundary conditions are considered (mic=True). Minimum and maximum distances are printed.
"""

from ase.build import bulk
from ase.neighborlist import NeighborList
import numpy as np

# Create a Cu FCC bulk with a 2x2x2 supercell
atoms = bulk('Cu', 'fcc', cubic=True)
atoms *= 8  # 2x2x2 supercell

# Neighbor list (periodic) – needed for mic (minimal image convention)
nl = NeighborList('12.0', skin=0.3, bothways=True, periodic=True)

# Tag atom 0 as "central" atom
ndt = np.ones(len(atoms), dtype=int)
ndt[0] = 0
atoms.set_tags(ndt)

# Build neighbor list with the central atom tagged
nl.update(atoms)

# Get distances; mic=True enforces the minimal image convention
distances = get_distances(atoms, atoms, indices=(0, ), mic=True)

idx_min = np.argmin(distances)
idx_max = np.argmax(distances)

print('Minimum distance:', distances[idx_min])
print('Maximum distance:', distances[idx_max])
