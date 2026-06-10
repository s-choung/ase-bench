from ase import Atoms
from ase.build import bulk
from ase.md import VelocityVerlet
from ase.calculators.emt import Emt
from ase.calculators.lj import LennardJones
from ase.constraints import FixScaled

# Create Al FCC 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.0, size=(2, 2, 2))

# Assign a built-in calculator (Lennard-Jones interaction)
atoms.set_calculator(LennardJones())

# Convert pressure from GPa to eV/Å^3
pressure = 10 * 10**9 * 1e-3 / (e*1e-18)  # GPa to eV/Å^3

# Set up the NPT ensemble using Berendsen thermostat and barostat
constraint = FixScaled(lattice=[1, 1, pressure], mask=[0, 0, 1])

# Attach the constraint to the atom's positions and velocities
md = VelocityVerlet(atoms, constraint)

# Initial volume
print(f"Initial volume: {atoms.get_cell().volume}")

# Run the MD simulation
md.run(100)

# Final volume
print(f"Final volume: {atoms.get_cell().volume}")
