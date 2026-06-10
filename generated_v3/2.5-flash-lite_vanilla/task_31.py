from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase import units

# Create Al FCC 2x2x2 supercell
atoms = fcc111('Al', size=(2, 2, 2), vacuum=10.0)

# Set EMT calculator
atoms.calc = EMT()

# Optimize initial structure with BFGS
opt = BFGS(atoms)
opt.run()

# Define NPT Berendsen thermostat and barostat
T = 500  # Temperature in Kelvin
P = 10   # Pressure in GPa
P_eV_Ang3 = P * units.GPa / units.eV * units.Ang**3 # Convert GPa to eV/Ang^3

dyn = NPTBerendsen(atoms,
                   timestep=1.0 * units.fs,
                   temperature=T * units.kB,
                   pressure=P_eV_Ang3,
                   ttime=0.5 * units.fs,
                   pbc=True)

# Record initial cell volume
initial_volume = atoms.get_volume()

# Run MD simulation for 100 steps
dyn.run(100)

# Record final cell volume
final_volume = atoms.get_volume()

# Print initial and final cell volumes
print(f"Initial cell volume: {initial_volume:.2f} Å³")
print(f"Final cell volume: {final_volume:.2f} Å³")
