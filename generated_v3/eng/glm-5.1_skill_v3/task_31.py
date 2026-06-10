from ase.build import bulk
from ase import units
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Al', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()

vol_init = atoms.get_volume()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

pressure_gpa = 10.0
pressure_eva3 = pressure_gpa / 160.2176634  # 1 eV/Ang^3 = 160.2176634 GPa

md = NPTBerendsen(atoms, timestep=5 * units.fs, temperature_K=500,
                  pressure=pressure_eva3, taut=50 * units.fs, taup=100 * units.fs)

md.run(100)

vol_final = atoms.get_volume()

print(f"Initial cell volume: {vol_init:.3f} Å³")
print(f"Final cell volume:   {vol_final:.3f} Å³")
