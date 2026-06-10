from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Al', 'fcc', a=4.05, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)

pressure_GPa = 10.0
pressure_eVA3 = pressure_GPa * units.GPa

print(f"Initial volume: {atoms.get_volume():.4f} Ang^3")

dyn = NPTBerendsen(atoms, timestep=1.0*units.fs, temperature_K=500,
                   pressure_au=pressure_eVA3, taut=100*units.fs,
                   taup=1000*units.fs, compressibility_au=4.57e-5/units.GPa)
dyn.run(100)

print(f"Final volume: {atoms.get_volume():.4f} Ang^3")
