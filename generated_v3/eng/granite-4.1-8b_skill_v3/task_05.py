from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.eos import EquationOfState
import numpy as np

# Step 1: Define a range of lattice constants around the experimental value for Cu (a₀ ≈ 3.615 Å)
lattice_constants = np.linspace(3.4, 3.8, 19)  # 3.4 to 3.8 Å in 18 steps
volumes = []
energies = []

# Step 2: Optimize each structure and collect data
for a in lattice_constants:
    atoms = bulk('Cu', 'fcc', a=a)
    atoms.calc = EMT()
    opt = BFGS(atoms)
    opt.run(fmax=0.05)
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

# Step 3: Fit to the Birch-Murnaghan EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Step 4: Calculate the equilibrium lattice constant from the equilibrium volume
# For FCC, the lattice constant a₀ is related to the cell volume V by V = (a₀³ / (4√2)).
# Therefore, a₀ = (3 * V / (4√2))^(1/3)
a_eq = ((3 * v0) / (4 * np.sqrt(2))) ** (1/3)

# Print the results
print(f"Equilibrium lattice constant (a₀): {a_eq:.6f} Å")
print(f"Equilibrium volume (V₀): {v0:.6f} Å³")
print(f"Bulk modulus (B): {B:.2f} GPa")
