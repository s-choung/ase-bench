from ase import Atoms
from ase.build import bulk
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.nptberendsen import NPTBerendsen
from ase.units import GPa, eV

# Convert pressure from GPa to eV/Ang^3
pressure = 10 * GPa / (eV / 1e-30)

# Create Al FCC 2x2x2 supercell
al = bulk('Al', 'fcc', a=4.05)
al = al.repeat((2, 2, 2))

# Set initial velocities
MaxwellBoltzmannDistribution(al, temperature_K=500)

# Initialize NPT Berendsen dynamics
dyn = NPTBerendsen(al, timestep=1 * fs, temperature_K=500, pressure=pressure, taut=0.1 * ps, taup=1.0 * ps)

# Print initial cell volume
print(f"Initial cell volume: {al.get_volume():.4f} Ang^3")

# Run NPT MD for 100 steps
for _ in range(100):
    dyn.run(1)

# Print final cell volume
print(f"Final cell volume: {al.get_volume():.4f} Ang^3")
