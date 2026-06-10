import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.eos import EquationOfState
from ase.calculators.emt import EMT

# Setup initial crystal
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

volumes = []
energies = []

# Sweep lattice constants around 3.6 Angstrom
for a in np.arange(3.4, 3.8, 0.05):
    atoms.set_cell([a, a, a])
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

# Fit to Equation of State
eos = EquationOfState(volumes, energies)
v0, e0, B, dBdv0 = eos.fit()

print(f"Equilibrium Volume: {v0:.3f} A^3")
print(f"Bulk Modulus: {B:.3f} eV/A^3")
