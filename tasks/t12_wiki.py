"""T12 Wiki: Build MoS2 monolayer"""
from ase.build import mx2

mos2 = mx2('MoS2', kind='2H', a=3.18, thickness=3.17, vacuum=10.0)
print(f"MoS2 atoms: {len(mos2)}, formula: {mos2.get_chemical_formula()}")
print(f"Cell: {mos2.get_cell()}")
print(f"PBC: {mos2.get_pbc()}")
