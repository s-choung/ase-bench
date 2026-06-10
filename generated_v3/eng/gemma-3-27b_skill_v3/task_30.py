from ase import Atoms
from ase.build import bulk
from ase.md.nptberendsen import NPTBerendsen
import ase.units as units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (3, 3, 3)
atoms.calc = EMT()

npt = NPTBerendsen(atoms, timestep=5 * units.fs, temperature_K=300, pressure=1 * units.bar,
                   taut=100 * units.fs, taup=1000 * units.fs)

initial_cell = atoms.get_cell()
initial_volume = initial_cell.volume()
initial_pressure = atoms.get_pressure()

npt.run(200)

final_cell = atoms.get_cell()
final_volume = final_cell.volume()
final_pressure = atoms.get_pressure()

print(f"Initial Cell Volume: {initial_volume:.6f} Å³")
print(f"Initial Pressure: {initial_pressure:.2f} bar")
print(f"Final Cell Volume: {final_volume:.6f} Å³")
print(f"Final Pressure: {final_pressure:.2f} bar")
