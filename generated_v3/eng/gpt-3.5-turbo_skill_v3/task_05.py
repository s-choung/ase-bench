from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimizers.bfgs import BFGS
from ase.eos import EquationOfState
import numpy as np

# Generate bulk Cu FCC structure
a = 3.6  # Initial guess for lattice constant
atoms = bulk('Cu', 'fcc', a=a)
atoms.calc = EMT()

# Optimize the lattice constant
optimizer = BFGS(atoms)
optimizer.run(fmax=0.01)

# Collect volumes and energies for EOS fitting
volumes = []
energies = []
for a in np.linspace(0.95, 1.05, 7):
    atoms = bulk('Cu', 'fcc', a=a)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

# Fit EOS to get equilibrium volume and bulk modulus
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

print(f"Equilibrium Volume: {v0:.2f} Å^3")
print(f"Bulk Modulus: {B:.2f} GPa")
