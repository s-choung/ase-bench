from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrate

h2o = molecule('H2O')
calc = EMT()
h2o.calc = calc
dyn = Vibrate(h2o, trajectory='h2o.traj')
dyn.run(nmodes=3)

for i, (freq, energy) in enumerate(zip(dyn.frequencies, dyn.energies)):
    print(f"Mode {i+1}: Frequency = {freq:.2f} cm^-1, Energy = {energy:.4f} eV")
