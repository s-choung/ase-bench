import numpy as np
from ase.build import bulk
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase import units

# 1. Setup System
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# 2. Geometry Optimization (Important for stable MD)
BFGS(atoms).run(fmax=0.01)

# 3. Initialize Velocities (300K)
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)  # Remove COM motion

# 4. Define Energy Helper
def get_total_energy(atoms):
    pe = atoms.get_potential_energy()
    ke = atoms.get_kinetic_energy()
    return pe + ke

# 5. Run NVE MD
initial_energy = get_total_energy(atoms)
dyn = VelocityVerlet(atoms, timestep=1 * units.fs)
dyn.run(50)
final_energy = get_total_energy(atoms)

# 6. Output Results
print(f"Initial Total Energy: {initial_energy:.6f} eV")
print(f"Final Total Energy:   {final_energy:.6f} eV")
print(f"Energy Drift:         {abs(final_energy - initial_energy):.6f} eV")
