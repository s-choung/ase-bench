from ase.build import fcc111
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase.md.langevin import Langevin
from ase.md.nvt import NVTBerendsen
from ase.units import fs
import numpy as np

atoms = fcc111('Cu', size=(3, 3, 3), vacuum=1.0)
atoms.set_cell([12.0, 12.0, 12.0], scale=1.0)

calculator = EMT()
atoms.set_calculator(calculator)

initial_volume = atoms.get_volume()
print(f"Initial volume: {initial_volume}")

nvt = NVTBerendsen(atoms, 300 * units.K, tau=100 * units.fs, taut=100 * units.fs, taup=1000 * units.fs, pressure=1 * units.bar)

dyn = VelocityVerlet(atoms, 5 * units.fs)
dyn.attach(nvt, 200)
dyn.run(200)

final_volume = atoms.get_volume()
final_pressure = atoms.get_potential_energy()/atoms.get_volume()
print(f"Final volume: {final_volume}")
print(f"Final pressure: {final_pressure}")
