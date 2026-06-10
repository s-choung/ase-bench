import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

atoms = bulk('Ag', 'fcc', a=4.08)
atoms.calc = EMT()

volumes, energies = [], []
cell = atoms.get_cell()

for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

a0 = v0**(1/3) if 'fcc' in bulk('Ag', 'fcc').get_chemical_symbols() else v0**(1/3) # Logic for cubic
# For FCC, V = a^3 / 4 is not the case in ASE bulk() as it returns conventional cubic cell
# ASE's bulk('Ag', 'fcc') returns a cubic cell where V = a^3
a_eq = v0**(1/3)

print(f"Equilibrium lattice constant: {a_eq:.4f} Å")
print(f"Bulk modulus: {B:.2f} GPa")
