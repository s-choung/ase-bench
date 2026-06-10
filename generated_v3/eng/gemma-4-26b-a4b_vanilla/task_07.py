import numpy as np
from ase import Atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase import units

# Setup Cu FCC bulk (using EMT as a placeholder for simplicity per constraints)
atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                          symbol='Cu', latticeconstant=3.6)
atoms.calc = EMT()

# Initialize velocities for 300K
temp = 300
velocities = np.random.normal(0, np.sqrt(3 * units.kB * temp / 1.0), atoms.shape[0, 3])
atoms.set_velocities(velocities)

def get_total_energy(atoms):
    return atoms.get_total_energy() + atoms.get_kinetic_energy()

e_init = get_total_energy(atoms)
print(f"Initial Total Energy: {e_init:.4f} eV")

# Run NVE MD
dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs)
dyn.run(50)

e_final = get_total_energy(atoms)
print(f"Final Total Energy:   {e_final:.4f} eV")
print(f"Energy Drift:         {abs(e_final - e_init):.4e} eV")
