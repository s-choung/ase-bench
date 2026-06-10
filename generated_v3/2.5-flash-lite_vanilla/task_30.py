from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units

# Create Cu FCC 3x3x3 supercell
atoms = fcc111('Cu', size=(3, 3, 3), vacuum=10.0)

# Set EMT calculator
atoms.calc = EMT()

# Set up NPT Berendsen dynamics
dyn = NPTBerendsen(atoms,
                    timestep=5 * units.fs,
                    temperature=300 * units.K,
                    pressure=0 * units.bar,  # Initial pressure is set to 0 for Berendsen
                    taut=100 * units.fs,
                    taup=1000 * units.fs)

# Print initial cell volume and pressure
print(f"Initial cell volume: {atoms.get_cell().volume:.2f} Å³")
print(f"Initial pressure: {atoms.get_pressure():.2f} bar")

# Run MD for 200 steps
dyn.run(200)

# Print final cell volume and pressure
print(f"Final cell volume: {atoms.get_cell().volume:.2f} Å³")
print(f"Final pressure: {atoms.get_pressure():.2f} bar")
