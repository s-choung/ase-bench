import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# reference FCC Cu
atoms = bulk('Cu', 'fcc', a=3.6)  # initial guess
calc = EMT()
atoms.calc = calc

# generate volumes around equilibrium
scale_factors = np.linspace(0.96, 1.04, 9)  # ±4% in length → ±12% in volume
volumes, energies = [], []

for s in scale_factors:
    a = atoms.copy()
    a.set_cell(a.get_cell() * s, scale_atoms=True)
    a.calc = calc
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

# fit EOS (Birch-Murnaghan)
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()  # B in eV/Å^3

# convert bulk modulus to GPa (1 eV/Å^3 = 160.21766208 GPa)
B_GPa = B * 160.21766208

print(f"Equilibrium volume per atom: {v0/4:.4f} Å^3")  # FCC has 4 atoms per cell
print(f"Equilibrium lattice constant: {(v0/4)**(1/3)*2**(1/2):.4f} Å")  # a = (V/4)^(1/3)*sqrt(2)
print(f"Bulk modulus: {B:.4f} eV/Å^3 ({B_GPa:.2f} GPa)")
