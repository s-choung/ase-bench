from ase.build import bulk
from ase.md.nptberendsen import NPTBerendsen
from ase.calculators.emt import EMT
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk("Al", "fcc", a=4.05).repeat((2, 2, 2))
atoms.calc = EMT()

pressure_ev_per_A3 = 10.0 * 1e9 * units.Pascal / (units.eV / units.Angstrom**3)

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=500,
    pressure=pressure_ev_per_A3,
    taut=100 * units.fs,
    taup=500 * units.fs,
)

initial_volume = atoms.get_volume()
dyn.run(100)
final_volume = atoms.get_volume()

print(f"Initial volume: {initial_volume:.2f} Å³")
print(f"Final volume: {final_volume:.2f} Å³")
