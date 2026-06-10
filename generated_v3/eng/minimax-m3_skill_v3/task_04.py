from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.io import write

atoms = molecule('H2O')
atoms.calc = EMT()

e0 = atoms.get_potential_energy()
print(f"Energy before: {e0:.4f} eV")

opt = BFGS(atoms, trajectory='h2o_opt.traj')
opt.run(fmax=0.01)

e1 = atoms.get_potential_energy()
print(f"Energy after:  {e1:.4f} eV")

write('H2O_optimized.xyz', atoms)
