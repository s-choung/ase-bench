from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = Atoms('H2O', positions=[[0.0, 0.0, 0.0], [0.757, 0.586, 0.0], [-0.757, 0.586, 0.0]])
atoms.calc = EMT()

initial_energy = atoms.get_potential_energy()
print(f'Initial energy: {initial_energy:.4f} eV')

dyn = BFGS(atoms)
dyn.run(fmax=0.05)

final_energy = atoms.get_potential_energy()
print(f'Final energy: {final_energy:.4f} eV')
