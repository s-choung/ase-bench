"""T12 Vanilla: Build MoS2 monolayer"""
from ase import Atoms

mos2 = Atoms('MoS2',
             positions=[(0, 0, 0), (1.59, 0.92, 1.58), (1.59, 0.92, -1.58)],
             cell=[[3.18, 0, 0], [1.59, 2.75, 0], [0, 0, 20.0]],
             pbc=[True, True, False])
print(f"MoS2 atoms: {len(mos2)}, formula: {mos2.get_chemical_formula()}")
print(f"Cell: {mos2.get_cell()}")
print(f"PBC: {mos2.get_pbc()}")
