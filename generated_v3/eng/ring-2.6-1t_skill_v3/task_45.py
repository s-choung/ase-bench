from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.geometry import get_distances
import numpy as np

atoms = molecule('H2')
atoms.calc = EMT()

d0 = np.linalg.norm(atoms.positions[1] - atoms.positions[0])
e0 = atoms.get_potential_energy()
print(f'Before FixBondLength: bond = {d0:.4f} Å, energy = {e0:.6f} eV')

atoms.set_positions(np.array([[0.0, 0.0, 0.0], [0.9, 0.0, 0.0]]))
atoms.set_constraint(FixBondLength(0, 1))

d1 = get_distances(0, 1, atoms.positions, cell=atoms.cell, pbc=atoms.pbc)[0][0]
e1 = atoms.get_potential_energy()
print(f'After  FixBondLength: bond = {d1:.4f} Å, energy = {e1:.6f} eV')
