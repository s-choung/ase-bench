from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Create Al fcc 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.05, cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

# Convert pressure: 10 GPa to eV/Ang^3
pressure = 10 * 1e9 * units.Pa  # Pa to internal units (eV/Ang^3)
# Alternatively: 10 * units.GPa (since units.GPa = 1e9 Pa)

# Set initial velocities
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Print initial volume
print(f"Initial volume: {atoms.get_volume():.2f} Å³")

# Run NPT MD
dyn = NPTBerendsen(atoms, timestep=1 * units.fs, 
                   temperature_K=500, taut=100 * units.fs,
                   pressure=pressure, taup=1000 * units.fs)
dyn.run(100)

# Print final volume
print(f"Final volume: {atoms.get_volume():.2f} Å³")
