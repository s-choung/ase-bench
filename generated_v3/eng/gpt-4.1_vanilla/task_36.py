import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

a0 = 4.09  # Ag FCC ref lattice [Å]
alat = np.linspace(0.95 * a0, 1.05 * a0, 7)

volumes = []
energies = []

for a in alat:
    ag = bulk('Ag', 'fcc', a=a)
    ag.calc = EMT()
    e = ag.get_potential_energy()
    v = ag.get_volume()
    energies.append(e)
    volumes.append(v)

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_eq = (v0 / 4) ** (1 / 3)  # FCC: 4 atoms/cell

from ase.units import kJ, GPa

B_GPa = B / (kJ * 1e21)  # ASE: B in eV/Å^3 -> J/m^3 == Pa; 1 GPa = 1e9 Pa

print(f'Equilibrium lattice constant: {a_eq:.4f} Å')
print(f'Bulk modulus: {B_GPa:.2f} GPa')
