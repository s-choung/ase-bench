from ase.build import bulk
from ase.constraints import FixScaledCell
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
import ase.units  # You'll use these units

# Create an FCC Al supercell
atoms = bulk('Al', 'fcc', size=(2,2,2))

# Set the calculator and initial cell constraints
atoms.calc = EMT()
atoms.set_constraint(FixScaledCell(constraints=10*ase.units.gPa))

# Set the temperature in Kelvin
T = 500 * units.kelvin

# MD Simulation setup
npt = NPTBerendsen(atoms=atoms, t_prescale=1.0, ttimescale=1.0, p0=10*units.giga/units.pascal, p_timescale=T)
npt.run(steps=100)

# Obtain initial and final cell volumes
initial_volume = atoms.get_cell_volume()
final_volume = npt.atoms.get_cell_volume()

print(f"Initial Cell Volume: {initial_volume: .2f} Å^3")
print(f"Final Cell Volume: {final_volume: .2f} Å^3")
