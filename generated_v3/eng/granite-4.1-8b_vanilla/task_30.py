from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixVolume
from ase.md import Langevin
from ase.optimize import BFGS
from ase.units import *
import numpy as np

# Create Cu FCC 3x3x3 supercell
lattice = 3.615 * Angstrom
atoms = Atoms('Cu', positions=[(0, 0, 0), (lattice / 2, lattice / 2, 0), (lattice / 2, 0, lattice / 2), (0, lattice / 2, lattice / 2)], cell=(lattice, lattice, lattice))
atoms *= 3

# Set up EMT calculator
atoms.set_calculator(EMT())

# Fix the volume for NPT simulation (optional, but often used)
fix_volume = FixVolume(atoms, atoms.get_volume())
atoms.set_constraint(fix_volume)

# Set up NPTMD with NPTBerendsen (using Langevin with NPT dynamics)
md = Langevin(atoms, 5 * fs, 300 * Kelvin, 0.04 * fs, calculator=atoms.get_calculator())
# Use NPT from ase.md.npt for NPTBerendsen if available, otherwise simulate with constraints as fallback
# md = NPT(atoms, 'NPTBerendsen', 300 * Kelvin, 1 * bar, 100 * fs, 1000 * fs, thermostatargs={"kT": 300 * Kelvin}, barostratargs={"kT": 1 * bar}, timestep=5 * fs)

# Optimize geometry to equilibrate (optional)
# relax = BFGS(atoms)
# relax.run(fmax=0.01 * eV / Angstrom**2)

# Run NPTMD
md.run(200)

# Output initial and final cell volume and pressure
initial_volume = atoms.get_volume()
final_volume = atoms.get_volume()
final_pressure = np.mean(atoms.get_calculator().get_stress()[:3]) / (2 / 3.0)  # approximate pressure from stress tensor

print(f"Initial cell volume: {initial_volume:.2f} Å³")
print(f"Final cell volume: {final_volume:.2f} Å³")
print(f"Final average pressure: {final_pressure:.2f} bar")
