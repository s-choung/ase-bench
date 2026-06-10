from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('CH4')

calc = EMT()
atoms.calc = calc

dyn = BFGS(atoms, trajectory='ch4_opt.traj')
dyn.run(fmax=0.02)

vib = Vibrations(atoms, calculator=calc)
vib.run()

real_frequencies = [freq for freq in vib.frequencies if freq > 0]
print(real_frequencies)
