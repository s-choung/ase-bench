from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Al', 'fcc', a=4.05).repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

press_gpa = 10.0
press_eV_per_A3 = press_gpa * 0.006241509  # 1 GPa = 0.006241509 eV/Å^3

print(f"Initial volume: {atoms.get_volume():.3f} Å^3")

dyn = NPTBerendsen(
    atoms,
    timestep=2.0 * units.fs,
    temperature_K=500,
    pressure_au=press_eV_per_A3,
    taut=100 * units.fs,
    taup=1000 * units.fs,
    compressibility_au=4.5e-6 / units.bar,  # Approx for Al
)
dyn.run(100)

print(f"Final volume: {atoms.get_volume():.3f} Å^3")
