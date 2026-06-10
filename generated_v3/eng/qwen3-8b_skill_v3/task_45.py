from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

atoms = Atoms('H2', positions=[[0.0, 0.0, 0.0], [1.0, 0.0, 0.0]])
atoms.calc = EMT()

initial_length = atoms.get_distances(0, 1)[0]
initial_energy = atoms.get_potential_energy()
print(f"Initial bond length: {initial_length} Å")
print(f"Initial energy: {initial_energy} eV")

atoms[1].position = (0.9, 0.0, 0.0)
constraint = FixBondLength(0, 1)
atoms.set_constraint([constraint])

adjusted_length = atoms.get_distances(0, 1)[0]
adjusted_energy = atoms.get_potential_energy()
print(f"Adjusted bond length: {adjusted_length} Å")
print(f"Adjusted energy: {adjusted_energy} eV")
