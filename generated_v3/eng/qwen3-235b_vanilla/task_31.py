from ase import Atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units

# Create Al FCC 2x2x2 supercell
atoms = FaceCenteredCubic(symbol='Al', size=(2,2,2))
atoms.calc = EMT()

# Set initial temperature and pressure
temp = 500
pressure_gpa = 10
pressure_ev = pressure_gpa * 1e9 * units.Pascal * (units.m**3) / (1e30 * units.Angstrom**3)  # Convert GPa to eV/Ang^3

# Print initial cell volume
print(f"Initial cell volume: {atoms.get_volume()} A^3")

# Setup NPT MD
dyn = NPTBerendsen(atoms, timestep=1*units.fs, temperature=temp*units.kB,
                   ttime=100*units.fs, pressure=pressure_ev, pfactor=100*units.fs,
                   trajectory=None)

# Run MD for 100 steps
for i in range(100):
    dyn.run(1)

# Print final cell volume
print(f"Final cell volume: {atoms.get_volume()} A^3")
