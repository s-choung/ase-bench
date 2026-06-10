from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

# FCC Au bulk (default lattice constant ~4.08 Å)
atoms = bulk('Au', 'fcc', a=4.08)
atoms.calc = EMT()

# Optimize geometry with LBFGS
opt = LBFGS(atoms)
opt.run(fmax=0.01)

print('Optimization steps:', opt.nsteps)
print('Final energy (eV):', atoms.get_potential_energy())
