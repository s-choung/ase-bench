from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase import units
import numpy as np

atoms = bulk('Pd', 'fcc', a=3.89).repeat([2, 2, 2])
atoms.calc = EMT()

atoms.set_temperature(500 * units.kB)
atoms.set_momenta(np.random.randn(len(atoms), 3) * np.sqrt(atoms.get_masses()[:, None] * units.kB * 500))

dyn = VelocityVerlet(atoms, 2 * units.fs)
e_initial = atoms.get_total_energy()

for _ in range(200):
    dyn.run(1)

e_final = atoms.get_total_energy()
print(f"Energy difference: {e_final - e_initial:.6f} eV")
