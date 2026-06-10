"""T2 Vanilla: Build FCC Cu bulk 2x2x2 supercell"""
from ase.lattice.cubic import FaceCenteredCubic

atoms = FaceCenteredCubic('Cu', latticeconstant=3.6, size=(2, 2, 2))
print(f"Number of atoms: {len(atoms)}")
print(f"Cell:\n{atoms.get_cell()}")
