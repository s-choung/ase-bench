```python
from ase import Atoms
from ase.calculators.emt import EMT
from ase.units import GPa
import numpy as np

# Reference FCC Ag lattice constant in Angstrom
a0 = 4.09
vol0 = a0**3
points = np.linspace(0.95, 1.05, 7)
energies, volumes = [], []

for factor in points:
    atoms = Atoms('Ag', positions=[(0,0,0)], cell=factor*a0*np.eye(3), pbc=True)
    atoms.set_calculator(EMT())
    energy = atoms.get_potential_energy()
    volumes.append(atoms.get_volume())
    energies.append(energy)

# Birch-Murnaghan EOS fit
def birch_murnaghan(V, E0, V0, B0, Bp):
    eta = (V0 / V)**(2./3)
    return E0 + 9*V0*B0/16 * (eta - 1)**2 * (6 + (4 - 3*eta)*(eta - 1))

from scipy.optimize import curve_fit
popt, _ = curve_fit(birch_murnaghan, volumes, energies, p0=[min(energies), vol0, 25*GPa, 4])
E0, V0, B0, Bp = popt[0], popt[1], popt[2]/GPa, popt[3]
a0_fit = V0**(1/3)

print(f'Equilibrium lattice constant: {a0_fit:.4f} A')
print(f'Bulk modulus: {B0:.2f} GPa')
