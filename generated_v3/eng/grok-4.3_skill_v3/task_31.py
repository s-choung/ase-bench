from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units
atoms = bulk('Al', 'fcc') * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)
p = 10 * units.GPa
dyn = NPTBerendsen(atoms, timestep=5*units.fs, temperature_K=500, pressure_au=p, taut=100*units.fs, taup=500*units.fs, compressibility_au=1/(100*units.GPa))
print(atoms.get_volume())
dyn.run(100)
print(atoms.get_volume())
