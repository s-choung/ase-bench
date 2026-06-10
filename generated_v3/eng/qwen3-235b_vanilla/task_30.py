from ase import Atoms
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.units import fs
import numpy as np

# Create 3x3x3 Cu FCC supercell
atoms = fcc111('Cu', size=(3, 3, 3), vacuum=0)
atoms.calc = EMT()

# Set initial temperature and NPT parameters
timestep = 5 * fs
temperature = 300
taut = 100 * fs
taup = 1000 * fs

# Create NPT dynamics
dyn = NPTBerendsen(atoms, timestep, temperature_K=temperature, taut=taut,
                   pressure_ar=1.0, taup=taup, logfile='npt.log')

# Print initial volume and pressure
print(f"Initial volume: {atoms.get_volume():.2f} A^3")
print(f"Initial pressure: {atoms.get_isotropic_pressure()*1e-9:.2e} GPa")

# Run 200 steps of NPT MD
dyn.run(200)

# Print final volume and pressure
print(f"Final volume: {atoms.get_volume():.2f} A^3")
print(f"Final pressure: {atoms.get_isotropic_pressure()*1e-9:.2e} GPa")
