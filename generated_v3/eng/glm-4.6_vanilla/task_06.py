from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.615).repeat((2, 2, 2))
atoms.calc = EMT()

def print_energy(a):
    print(f"Step: {a.get_number_of_atoms()}, T: {a.get_temperature():.1f} K, E: {a.get_total_energy()/(len(a)):.3f} eV/atom")

print("Initial state:")
print_energy(atoms)

dyn = Langevin(atoms, timestep=5*units.fs, temperature=300*units.kB, friction=0.002)
dyn.run(100)

print("\nFinal state:")
print_energy(atoms)
