from ase import Atoms, units
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Initialize Cu FCC
cu = Atoms('Cu', positions=[(0, 0, 0)], cell=(3.6*units.Bohr,)*3, pbc=True)

# EOS parameters
ratios = np.linspace(0.95, 1.05, 6)
V_data, E_data = [], []

# Calculate energies
for sc in ratios:
    scaled = cu.copy()
    scaled.set_cell([sc*x for x in cu.get_cell()], scale_atoms=True)
    scaled.calc = EMT()
    V_data.append(scaled.get_volume())
    E_data.append(scaled.get_potential_energy())

# Fit EOS
eos = EquationOfState(V_data, E_data)
v0, e0, B = eos.fit()

# Output
print(f"Equilibrium Volume: {v0:.6f} Å³")
print(f"Bulk Modulus: {B/units.GPa:.3f} GPa")
