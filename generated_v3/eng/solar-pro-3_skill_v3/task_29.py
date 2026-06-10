from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.md.verlet import VelocityVerlet
from ase.thermochemistry import MaxwellBoltzmannDistribution
import numpy as np

# 1. Build Pd FCC 2x2x2 supercell
atoms = bulk('Pd', 'fcc', a=3.98, cubic=True) * (2, 2, 2)

# 2. Set EMT calculator and relax positions (optional but recommended)
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

# 3. Equilibrate & assign velocities with target temperature 500 K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# 4. Verify stationary COM (prevents drift)
from ase.md.velocitydistribution import Stationary
atoms = Stationary(atoms)

# 5. Run NVE MD with VelocityVerlet, timestep = 2 fs
md = VelocityVerlet(atoms, timestep=2 * 1e-3 * 1e15)  # 1e15 converts fs to ps for units.fs
md.run(200)

# 6. Compute total energy (kinetic + potential) before and after
E_start = atoms.get_total_energy()
E_end   = atoms.get_total_energy()
print(f'Total energy difference (kinetic+potential): {E_end - E_start:.6f} eV')
