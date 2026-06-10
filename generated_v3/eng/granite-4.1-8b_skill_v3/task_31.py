from ase import Atoms
from ase.build import bulk, make_supercell
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.constraints import FixAtoms
from ase.units import GPa, eV, Angstrom, kelvin
import numpy as np

# Initial FCC aluminum lattice parameter
al = bulk('Al', 'fcc', a=4.05)  # lattice constant of Al in Å
# Create a 2x2x2 supercell
supercell = make_supercell(al, [[2, 0, 0], [0, 2, 0], [0, 0, 2]])

# Convert pressure from GPa to eV/Ang^3
pressure_GPa = 10.0
pressure_ev_per_ang3 = pressure_GPa * 1e9 * 160.217648 # GPa to atm, atm to eV/Ang^3
print(f"Input pressure: {pressure_GPa} GPa = {pressure_ev_per_ang3:.2f} eV/Ang^3")

# Assign EMT calculator
supercell.calc = EMT()

# Optionally, fix the atoms to speed up the NPT run (not necessary here)
# fix = FixAtoms(mask=[atom.tag != -1 for atom in supercell])
# supercell.set_constraint(fix)

# Set up NPTBerendsen MD
md = NPTBerendsen(supercell,
                  temp=500.0,  # temperature in Kelvin
                  pressure=pressure_ev_per_ang3,  # pressure in eV/Ang^3
                  length=10,  # time step in fs
                  aytpe='triclinic',  # or 'ortho' for orthorhombic cells
                  nruns=100)   # number of MD steps

# Run the MD
md.run()

# Print initial and final cell volume
initial_volume = supercell.get_volume()
final_volume = md.atoms.get_volume()
print(f"Initial cell volume (Å^3): {initial_volume:.3f}")
print(f"Final cell volume (Å^3):   {final_volume:.3f}")
