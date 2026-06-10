import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', cubic=True).repeat((3, 3, 3))
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
stress = atoms.get_stress()
print(atoms.get_volume(), -np.mean(stress[:3])/units.bar)
dyn = NPTBerendsen(atoms, 5*units.fs, temperature_K=300, pressure_au=1*units.bar, taut=100*units.fs, taup=1000*units.fs)
dyn.run(200)
stress = atoms.get_stress()
print(atoms.get_volume(), -np.mean(stress[:3])/units.bar)
