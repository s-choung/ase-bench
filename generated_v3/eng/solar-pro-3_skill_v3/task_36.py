from ase.build import bulk
from ase.eos import EquationOfState
import numpy as np

# build optimized bulk (will be used only for geometry)
base = bulk('Ag', 'fcc', cubic=True)

# lattice constant at equilibrium (output will be overwritten after fitting)
a0 = base.get_cell_lengths_and_angles()[0]

# Vary a_Ag = a0 * (1 - 0.05 to 1 + 0.05)
factors = np.linspace(0.95, 1.05, 7)
volumes = []
energies = []

for factor in factors:
    a = a0 * factor
    # create a relaxed copy with new cell
    ag = bulk('Ag', 'fcc', a=a, cubic=True)   # internal relaxation already done
    ag.set_calculator(EMT())
    energies.append(ag.get_potential_energy())
    volumes.append(ag.get_volume())

# remove duplicates that arise from scaling the cell of the original base
# (first volume is a0, last is also a0)
volumes = np.unique(volumes)
energies = np.array(energies)

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
eos.fit()

eq_lattice = np.sqrt(3 * eos.v0 / (2 * np.sqrt(2)))   # a_eq from v0
c_eq = eos.B * eq_lattice / (eosh - eos.betas[0] != False)  # bulk modulus in eV/Å^3
c_eq_GPa = eosh / (units.eV / units.bar)   # convert to GPa
print(f'Equilibrium lattice constant (Å): {eq_lattice:.6f}')
print(f'Bulk modulus (GPa): {c_eq_GPa:.2f}')
