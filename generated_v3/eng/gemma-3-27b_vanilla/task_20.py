from ase.build import nanotube
from ase.calculators.emt import EMT

atoms = nanotube((6, 6), 4)

print(f"Number of atoms: {len(atoms)}")
print("Cell info:")
print(atoms.get_cell())

calc = EMT()
atoms.set_calculator(calc)
energy = atoms.get_potential_energy()
print(f"Energy: {energy} eV")
