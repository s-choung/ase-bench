from ase import Atoms
from ase.calculators.emt import EMT
from ase.calculators.lj import LJC
from ase.gauss import Gaussian
from ase.build import molecule
from ase.optimize import BFGS

c = EMT()
a = molecule('CH4')
a.calc = c
a.get_potential_energy()
opt = BFGS(a, trajectory='ch4_opt.traj')
opt.run(fmax=0.01)

c.set_kpts([2,2,2])
a.calc = c
freqs = a.get_frequencies()

for freq in freqs:
    if freq > 0:
        print(freq)
