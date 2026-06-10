from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.io import read, write

atoms = Atoms('H2O', positions=[[0, 0, 0], [1, 0, 0], [0, 1, 0]])
atoms.calc = EMT()

print(f"Initial energy: {atoms.get_potential_energy():.6f} eV")

dyn = BFGS(atoms, trajectory='h2o_opt.traj')
dyn.run(fmax=0.01)

print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
write('h2o_optimized.xyz', atoms)
