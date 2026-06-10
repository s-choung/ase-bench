from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import NPTBerendsen
from ase.units import eV, Angstrom, fs

# Create Al FCC 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.05, cubic=True, size=(2,2,2))
atoms.calc = EMT()

# Initial volume
initial_volume = atoms.get_volume()

# Convert pressure from GPa to eV/Ang^3
pressure_GPa = 10
pressure_eV_Ang3 = pressure_GPa * 6.242e-3  # 1 GPa = 6.242e-3 eV/Ang^3

# Set up NPTBerendsen
md = NPTBerendsen(atoms, dt=10*fs, temperature_K=500, pressure=pressure_eV_Ang3, compressibility=0.1)

# Run MD for 100 steps
md.run(100)

# Final volume
final_volume = atoms.get_volume()

# Print results
print(f"Initial volume: {initial_volume} Å³")
print(f"Final volume: {final_volume} Å³")
