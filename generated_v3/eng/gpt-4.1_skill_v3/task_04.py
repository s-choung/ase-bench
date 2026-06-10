from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = molecule('H2O')
atoms.calc = EMT()
e0 = atoms.get_potential_energy()
print(f'Initial energy: {e0:.6f} eV')
BFGS(atoms).run(fmax=0.01)
e1 = atoms.get_potential_energy()
print(f'Final energy:   {e1:.6f} eV')
