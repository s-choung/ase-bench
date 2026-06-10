import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# Initial cubic cell (4 atoms)
atoms = bulk('Cu', 'fcc', a=3.6)
cell = atoms.get_cell()

volumes = []
energies = []

# Scale volume isotropically around initial guess
for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()  # v0 in Å³, B in eV/Å³

B_GPa = B * 160.21766208  # 1 eV/Å³ to GPa

print(f"Equilibrium volume: {v0:.4f} Å³")
print(f"Bulk modulus: {B:.4f} eV/Å³ ({B_GPa:.2f} GPa)")
