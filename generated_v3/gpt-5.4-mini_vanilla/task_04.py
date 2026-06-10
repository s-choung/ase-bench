from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = Atoms('H2O', positions=[(0.0, 0.0, 0.0), (0.96, 0.0, 0.0), (-0.24, 0.93, 0.0)])
atoms.calc = EMT()

e0 = atoms.get_potential_energy()
print(f"Initial energy: {e0:.6f} eV")

opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.05)

e1 = atoms.get_potential_energy()
print(f"Final energy: {e1:.6f} eV")
