from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.phonons import Phonons
from ase.thermodynamics import HarmonicThermo

cu = bulk('Cu', 'fcc', a=3.61)
calc = EMT()
cu.calc = calc
dyn = BFGS(cu, trajectory='cu.traj')
dyn.run(forceseterr=1e-3)

phonons = Phonons(cu, calculator=calc)
phonons.run()

thermo = HarmonicThermo(phonons)
f = thermo.get_helmholtz_free_energy(temperature=300)
print(f)
