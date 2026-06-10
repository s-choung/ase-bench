from ase import Atoms
from ase.optimizers import BFGS
from ase.calculators.emt import EMT

atoms = Atoms('Au', cell=[4.08,4.08,4.08], pbc=True)
atoms.calc = EMT()
opt = LBFGS(atoms, logfile=None)
opt.run(fmax=0.01)
print(f"Steps: {opt.nsteps}, Energy: {atoms.get_potential_energy():.3f} eV")
