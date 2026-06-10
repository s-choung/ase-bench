from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Al', 'fcc', a=4.05, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

T = 500
P = 10 * units.GPa  # eV/Ang^3

MaxwellBoltzmannDistribution(atoms, temperature_K=T)

dyn = NPTBerendsen(atoms, timestep=1 * units.fs,
                   temperature_K=T,
                   pressure_au=P,
                   taut=100 * units.fs,
                   taup=1000 * units.fs,
                   compressibility_au=1 / (76 * units.GPa))

print(f"Initial volume: {atoms.get_volume():.3f} Ang^3")
dyn.run(100)
print(f"Final volume:   {atoms.get_volume():.3f} Ang^3")
