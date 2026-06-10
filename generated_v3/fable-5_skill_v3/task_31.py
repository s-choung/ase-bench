from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Al', 'fcc', a=4.05, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

pressure = 10 * units.GPa  # 10 GPa -> eV/Ang^3
v0 = atoms.get_volume()
print(f"Initial volume: {v0:.3f} Ang^3")

dyn = NPTBerendsen(
    atoms,
    timestep=2 * units.fs,
    temperature_K=500,
    pressure_au=pressure,
    taut=100 * units.fs,
    taup=1000 * units.fs,
    compressibility_au=1.0 / (76 * units.GPa),  # Al bulk modulus ~76 GPa
)
dyn.run(100)

v1 = atoms.get_volume()
print(f"Final volume:   {v1:.3f} Ang^3")
print(f"Final temperature: {atoms.get_temperature():.1f} K")
