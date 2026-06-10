from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = molecule('H2O')
atoms.calc = EMT()

E_initial = atoms.get_potential_energy()
print(f"Initial energy: {E_initial:.6f} eV")

opt = BFGS(atoms)
opt.run(fmax=0.05)

E_final = atoms.get_potential_energy()
print(f"Final energy: {E_final:.6f} eV")
print(f"Energy change: {E_final - E_initial:.6f} eV")
