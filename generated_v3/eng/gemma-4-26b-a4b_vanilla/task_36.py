import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# Note: EMT is for transition metals but not parameterized for Ag. 
# Using EMT as requested by constraints, though results will be physically inaccurate for Ag.
atoms = bulk('Ag', 'fcc', a=4.08)
atoms.calc = EMT()

a0 = atoms.get_cell().lengths()[0]
a_range = np.linspace(a0 * 0.95, a0 * 1.05, 7)
energies = []

for a in a_range:
    atoms.set_cell([a, a, a])
    atoms.set_pbc(True)
    energies.append(atoms.get_total_energy())

eos = EquationOfState(a_range, energies)
v0, b0 = eos.fit()

# Convert V0 (volume) to lattice constant a
a_eq = v0**(1/3)

# Conversion factor: 1 eV/A^3 to GPa is ~160.21766
# B0 is in eV/A^3
b0_gpa = b0 * 160.21766

print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Bulk modulus: {b0_gpa:.2f} GPa")
