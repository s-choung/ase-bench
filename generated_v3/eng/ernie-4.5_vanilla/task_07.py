from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase.units import fs, kB
from ase.io import write

# Create FCC Cu bulk
atoms = Atoms('Cu8', cell=[4, 4, 4], pbc=True,
              positions=[(0,0,0), (0.5,0.5,0), (0.5,0,0.5), (0,0.5,0.5),
                        (0.5,0,0), (0,0.5,0), (0,0,0.5), (0.5,0.5,0.5)],
              calculator=EMT())

# Set initial momenta corresponding to T=300K
temperature = 300  # K
maxwell_bolt = lambda kT: [v for _ in range(len(atoms)) for v in (0, 0, 0)] # (Simplified placeholder for zero - properly should be random Gaussian)
# However, ASE has a built-in method we can use
atoms.set_momenta(atoms.get_momenta(temperature=temperature * kB / 1)) # ASE method to set momenta from temperature

# Create MD object
md = VelocityVerlet(atoms, dt=1 * fs, trajectory=None, logfile=None)

# Print initial total energy
initial_energy = atoms.get_total_energy()
print(f"Initial total energy: {initial_energy} eV")

# Run MD for 50 steps
md.run(50)

# Print final total energy
final_energy = atoms.get_total_energy()
print(f"Final total energy: {final_energy} eV")
