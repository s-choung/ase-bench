from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = molecule('H2O')
atoms.calc = EMT()

initial_energy = atoms.get_potential_energy()
print(f"Initial energy: {initial_energy:.6f} eV")

optimizer = BFGS(atoms)
optimizer.run(fmax=0.01)

final_energy = atoms.get_potential_energy()
print(f"Final energy: {final_energy:.6f} eV")
