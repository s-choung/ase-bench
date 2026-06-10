from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

n2 = molecule('N2')
calc = EMT()
n2.calc = calc

opt = BFGS(n2, trajectory='n2_emt.traj')
opt.run(fmax=0.01)

from ase.vibrations import vibrational_frequencies
frequencies = vibrational_frequencies(n2)

print(frequencies)
