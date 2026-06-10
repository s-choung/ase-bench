import numpy as np
from ase import Atoms, units
from ase.md.nptberendsen import NPTBerendsen
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Create Cu FCC 3x3x3 supercell
atoms = Atoms('Cu', cell=3.6*np.eye(3), pbc=True)
atoms = atoms.repeat((3, 3, 3))

# Setup calculator
atoms.calc = EMT()

# Initialize velocities for 300K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Setup NPTBerendsen
md = NPTBerendsen(atoms, timestep=5*units.fs,
                  temperature_K=300, pressure_au=1*units.bar,
                  taut=100*units.fs, taup=1000*units.fs)

# Print initial state
initial_vol = atoms.get_volume()
initial_p = -np.trace(atoms.get_stress(voigt=False)) / 3
print(f'Initial: volume={initial_vol:.2f} Å³, pressure={initial_p:.4f} eV/Å³')

# Run MD
md.run(200)

# Print final state
final_vol = atoms.get_volume()
final_p = -np.trace(atoms.get_stress(voigt=False)) / 3
print(f'Final: volume={final_vol:.2f} Å³, pressure={final_p:.4f} eV/Å³')
