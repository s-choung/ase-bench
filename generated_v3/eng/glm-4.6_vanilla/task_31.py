from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import NPTBerendsen

# Create Al FCC 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.05, cubic=True) * [2, 2, 2]
atoms.calc = EMT()

# Convert 10 GPa to eV/Ang^3 (1 GPa = 1/160.21766208 eV/Ang^3)
pressure = 10.0 / 160.21766208

# Initialize NPT dynamics
dyn = NPTBerendsen(atoms, timestep=1.0, temperature_K=500,
                   pressure_au=pressure, taut=0.5, taup=1.0,
                   compressibility_au=1e-5)

# Print initial volume
print(f"Initial Volume: {atoms.get_volume():.3f} Å^3")

# Run MD for 100 steps
dyn.run(100)

# Print final volume
print(f"Final Volume: {atoms.get_volume():.3f} Å^3")
