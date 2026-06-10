from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6) * (3, 3, 3)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

p0 = atoms.get_pressure()
print(f"Initial volume:   {atoms.get_volume():.3f} A^3")
print(f"Initial pressure: {p0:.6f} eV/A^3")

dyn = NPTBerendsen(atoms, timestep=5*units.fs, temperature_K=300,
                   pressure=1.0*units.bar,
                   taut=100*units.fs, taup=1000*units.fs,
                   trajectory='npt.traj', logfile='npt.log')
dyn.run(200)

p1 = atoms.get_pressure()
print(f"Final volume:   {atoms.get_volume():.3f} A^3")
print(f"Final pressure: {p1:.6f} eV/A^3")
