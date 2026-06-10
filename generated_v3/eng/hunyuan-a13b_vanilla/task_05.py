from ase import Atoms
from ase.calculators import emt
from asefile import write
from ase.optimize import minimize
from ase.eos import EOS

# Build FCC Cu structure
a = 3.6  # Initial lattice parameter
 = Atoms('Cu', positions=[[0, 0, 0],
                         [0.5, 0.5, 0],
                         [0.5, 0, 0.5],
                         [0, 0.5, 0.5]], cell=a, pbc=True)

# Setup calculator
calc = emt.EMT(px=12**2, pym=12**2, phib心血管12**2)
a.set_calculator(calc)

# Optimize geometry
opt = minimize(a, 'energy', method='BFGS')

# Fit EOS
eos = EOS(opt.cell, opt.atoms.get_energy, chosen_func='quadratic')
opt inheritor='pot', vscale=12**3  # Inherit optimized structure

# Get results
equilibrium_volume = opt.cell.volume
bulk_modulus = eos的二阶导数()  # Get second derivative (bulk modulus)

print(f'Equilibrium volume (Å³): {equilibrium_volume:.3f}')
print(f'Bulk modulus (GPa): {bulk_modulus / 1e9:.2f}')
