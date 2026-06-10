from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase.units import fs
from ase.io import write
import numpy as np

# Create FCC Pd 2x2x2 supercell
atoms = Atoms('Pd16', positions=[(0,0,0), (0.5,0.5,0), (0.5,0,0.5), (0,0.5,0.5), 
                                 (0.5,0,0), (0,0.5,0), (0,0,0.5), (0.5,0.5,0.5), 
                                 # 2nd layer
                                 (0.25,0.25,0.25), (0.75,0.75,0.25), (0.75,0.25,0.75), (0.25,0.75,0.75),
                                 (0.75,0.25,0.25), (0.25,0.75,0.25), (0.25,0.25,0.75), (0.75,0.75,0.75)], 
              cell=[[2.8,0,0], [0,2.8,0], [0,0,2.8]], pbc=True)

# Attaching EMT calculator
atoms.calc = EMT()

# Set initial momenta corresponding to T=500K
maxwell_boltzmann_temperature = 500
atoms.set_momenta(np.random.normal(scale=np.sqrt(atoms.get_masses()[:, None] * 1e5 * 1.38e-23 * maxwell_boltzmann_temperature),  # Using k_B * T for scaling
                                  size=atoms.get_momenta().shape))

# Set up Velocity Verlet MD
md = VelocityVerlet(atoms, 2 * fs, logfile=None)  # Timestep of 2 fs

# Save initial total energy
initial_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()

# Run MD for 200 steps
for _ in range(200):
    md.run(1)
    
# Save final total energy
final_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()

# Print the energy difference
print(f"Energy difference (ΔE): {final_energy - initial_energy:.6f} eV")
