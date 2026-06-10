from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.npt_berendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Cu', 'fcc', a=3.615) * (3, 3, 3)
atoms.calc = EMT()

print("Initial cell volume:", atoms.get_volume(), "A^3")
print("Initial pressure:", atoms.get_pressure(), "eV/A^3")

MaxwellBoltzmannDistribution(atoms, temperature_K=300)

dyn = NPTBerendsen(atoms, timestep=5*units.fs, temperature=300, pressure=1*units.bar,
                   taut=100*units.fs, taup=1000*units.fs)
dyn.run(200)

print("Final cell volume:", atoms.get_volume(), "A^3")
print("Final pressure:", atoms.get_pressure(), "eV/A^3")
