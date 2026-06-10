#!/usr/bin/env python3
"""
Create a Cu FCC bulk, generate a 2×2×2 supercell,
and print cell parameters and atom count.
"""

from ase.build import bulk

# Cu FCC bulk (default lattice constant ~3.6 Å)
cu = bulk('Cu', 'fcc')

# 2×2×2 supercell
cu_super = cu * (2, 2, 2)   # repeat along a, b, c

# Output
print("Cell vectors (Å):")
print(cu_super.get_cell())
print("Number of atoms:", len(cu_super))
