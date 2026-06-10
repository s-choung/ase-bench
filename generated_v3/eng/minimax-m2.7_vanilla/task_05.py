import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# Scan lattice constants around the expected equilibrium
a_vals = np.linspace(3.40, 3.90, 12)

volumes, energies = [], []
for a in a_vals:
    cu = bulk('Cu', 'fcc', a=a)
    cu.set_calculator(EMT())
    energies.append(cu.get_potential_energy())
    volumes.append(cu.get_volume())

# Fit Equation of State
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()           # v0 in Å³ (conventional cell), B in eV/Å³

# Convert bulk modulus to GPa
B_GPa = B * 160.2176634

# Equilibrium lattice constant (conventional cubic cell)
a_eq = v0 ** (1/3)

# Volume per atom (fcc conventional cell contains 4 atoms)
vol_per_atom = v0 / 4

print(f"Equilibrium lattice constant a = {a_eq:.4f} Å")
print(f"Equilibrium volume per atom   = {vol_per_atom:.4f} Å³")
print(f"Bulk modulus B                = {B_GPa:.2f} GPa")
