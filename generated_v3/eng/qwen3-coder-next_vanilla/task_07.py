from ase import Atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.units import kB
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.langevin import Langevin
from ase.calculators.emt import EMT

# Create Cu FCC bulk unit cell
atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], 
                          symbol='Cu', latticeconstant=3.61, size=(2, 2, 2))

# Set EMT calculator
atoms.calc = EMT()

# Set initial temperature
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Get initial total energy
initial_energy = atoms.get_total_energy()

# Run NVE MD using VelocityVerlet (via Langevin with zero friction)
dampingscale = 1e6  # Very large damping to effectively simulate NVE
dyn = Langevin(atoms, timestep=1.0*units.fs, temperature_K=300, friction=dampingscale)

# Run 50 steps
dyn.run(50)

# Get final total energy
final_energy = atoms.get_total_energy()

# Print energies
print(f"Initial total energy: {initial_energy:.6f} eV")
print(f"Final total energy: {final_energy:.6f} eV")
