import numpy as np
from ase import Atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.md.velocityverlet import VelocityVerlet
from ase.md.constants import kB
from ase.calculators.emt import EMT

# Parameters
temp = 500
timestep = 2 * 1.0  # fs (ASE uses units consistent with calculator, here we assume eV, fs, amu)
n_steps = 200

# Setup Pd FCC 2x2x2 supercell
# Note: EMT is for transition metals like Pd/Cu/Ni; Pd is not strictly in EMT 
# but EMT is the standard ASE built-in for metallic-like potentials.
atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], 
                          symbol='Pd', size=(2, 2, 2), latticeconstant=3.89)
atoms.calc = EMT()

# Initialize velocities
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
MaxwellBoltzmannDistribution(atoms, temperature_K=temp)

def get_total_energy(atoms):
    return atoms.get_kinetic_energy() + atoms.get_potential_energy()

e_start = get_total_energy(atoms)

# Run MD
dyn = VelocityVerlet(atoms, timestep=timestep)
dyn.run(n_steps)

e_end = get_total_energy(atoms)

print(f"Initial Total Energy: {e_start:.6f} eV")
print(f"Final Total Energy:   {e_end:.6f} eV")
print(f"Energy Drift:         {abs(e_end - e_start):.6f} eV")
