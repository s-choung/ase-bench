from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

gpa_to_ev_a3 = 1.0 / 160.21766208
pressure = 10.0 * gpa_to_ev_a3
compressibility = 1.0 / (76.0 * gpa_to_ev_a3)

atoms = bulk("Al", "fcc", a=4.05, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

print(f"Pressure: {pressure:.6f} eV/Ang^3")
print(f"Initial volume: {atoms.get_volume():.6f} Ang^3")

dyn = NPTBerendsen(
    atoms,
    timestep=1.0 * units.fs,
    temperature_K=500,
    taut=100.0 * units.fs,
    pressure_au=pressure,
    taup=1000.0 * units.fs,
    compressibility_au=compressibility,
)

dyn.run(100)

print(f"Final volume: {atoms.get_volume():.6f} Ang^3")
