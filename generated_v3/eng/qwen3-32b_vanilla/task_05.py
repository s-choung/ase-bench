import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

volumes, energies = [], []
for a in np.linspace(3.5, 4.0, 8):
    cu = bulk('Cu', 'fcc', a=a)
    cu.calc = EMT()
    volumes.append(cu.get_volume())
    energies.append(cu.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
print(f"Equilibrium volume: {v0} Å³")
print(f"Bulk modulus: {B} GPa")
print(f"Equilibrium lattice constant: {v0**(1/3)} Å")
