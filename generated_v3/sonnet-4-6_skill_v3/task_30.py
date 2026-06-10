import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase.md.nptberendsen import NPTBerendsen

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (3, 3, 3)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
ZeroRotation(atoms)

initial_volume = atoms.get_volume()
stress = atoms.get_stress(voigt=True)
initial_pressure = -stress[:3].mean() / units.bar

print(f"Initial volume: {initial_volume:.4f} Å³")
print(f"Initial pressure: {initial_pressure:.4f} bar")

dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    pressure_au=1 * units.bar,
    taut=100 * units.fs,
    taup=1000 * units.fs,
    compressibility_au=4.57e-5 / units.bar,
)

dyn.run(200)

final_volume = atoms.get_volume()
stress = atoms.get_stress(voigt=True)
final_pressure = -stress[:3].mean() / units.bar

print(f"\nFinal volume: {final_volume:.4f} Å³")
print(f"Final pressure: {final_pressure:.4f} bar")
print(f"Volume change: {final_volume - initial_volume:.4f} Å³ ({(final_volume/initial_volume - 1)*100:.3f}%)")
