from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.61, repeat=(3, 3, 3))
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

initial_vol = atoms.get_volume()
stress = atoms.get_stress()
press_conv = units.eV / units.Angstrom**3 / units.bar
initial_press = -np.trace(stress) / 3 * press_conv

dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    pressure=1.0,
    taut=100 * units.fs,
    taup=1000 * units.fs
)
dyn.run(200)

final_vol = atoms.get_volume()
stress = atoms.get_stress()
final_press = -np.trace(stress) / 3 * press_conv

print(f"Initial volume: {initial_vol:.2f} Å³")
print(f"Initial pressure: {initial_press:.2f} bar")
print(f"Final volume: {final_vol:.2f} Å³")
print(f"Final pressure: {final_press:.2f} bar")
