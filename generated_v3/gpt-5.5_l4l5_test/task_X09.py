from ase.build import fcc111
from ase.calculators.emt import EMT
import numpy as np

slab = fcc111("Al", size=(1, 1, 6), vacuum=15.0)
slab.calc = EMT()
slab.get_potential_energy()

try:
    e_fermi = slab.get_fermi_level()
    e_vacuum = slab.calc.get_electrostatic_potential().max()
    work_function = e_vacuum - e_fermi
except Exception:
    work_function = np.nan

print(f"{work_function:.6f} eV")
