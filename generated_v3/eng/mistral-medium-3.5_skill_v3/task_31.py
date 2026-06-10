from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Al', 'fcc', a=4.05) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)
P_target = 10 * units.GPa / units.eV * (units.Bohr**3) / (units.Ang**3)
NPTBerendsen(atoms, timestep=5*units.fs, temperature_K=500,
             pressure=P_target, taut=0.1*units.ps, taup=0.1*units.ps).run(100)
print(atoms.get_volume(), atoms.get_volume())
