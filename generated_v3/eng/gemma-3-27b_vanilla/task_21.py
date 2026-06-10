from ase.build import icosahedron
from ase.calculators.emt import EMT
from ase.calculators.lj import LennardJones
import numpy as np

atoms = icosahedron(size=(3, 3, 3), shell_layers=3, symbol='Au')

print(len(atoms))
print(atoms.get_center_of_mass())

calc = EMT()
atoms.set_calculator(calc)
energy = atoms.get_potential_energy()
print(f"EMT Energy: {energy} eV")

calc = LennardJones()
atoms.set_calculator(calc)
energy = atoms.get_potential_energy()
print(f"LJ Energy: {energy} eV")
