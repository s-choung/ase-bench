from ase.build import bulk
from ase.calculators.emt import EMT

a = 3.3
atoms = bulk('Al', 'bcc', a=a, cubic=True)
print(atoms.cell)
print(atoms.get_chemical_formula())

calc = EMT()
atoms.set_calculator(calc)
energy = atoms.get_potential_energy()
print(f"Energy: {energy} eV")
