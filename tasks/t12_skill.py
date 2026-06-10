"""T12 Skill: Build MoS2 monolayer"""
from ase.build import molecule

mos2 = molecule('MoS2')
print(f"MoS2 atoms: {len(mos2)}, formula: {mos2.get_chemical_formula()}")
print(f"Positions:\n{mos2.get_positions()}")
