import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.visualize import view

# Build Cu FCC bulk
atoms = bulk('Cu','fcc',a=3.6, cubic=True, orthorhombic=True)
atoms.calc = EMT()

# Fit EOS
cell = atoms.get_cell()
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# Print results
print(f"Equilibrium Volume: {v0} Å³")
print(f"Bulk Modulus: {B} GPa")

# Visualize (optional)
# view(atoms)
