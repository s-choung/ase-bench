from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', cubic=True) * (3, 3, 3)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

print(f"Initial volume: {atoms.get_volume():.3f} Å³, pressure: {atoms.get_pressure()/units.bar:.3f} bar")

dyn = NPTBerendsen(atoms, timestep=5*units.fs, temperature_K=300,
                   pressure=1*units.bar, taut=100*units.fs,
                   taup=1000*units.fs, compressibility=7e-7)
dyn.run(200)

print(f"Final volume: {atoms.get_volume():.3f} Å³, pressure: {atoms.get_pressure()/units.bar:.3f} bar")
