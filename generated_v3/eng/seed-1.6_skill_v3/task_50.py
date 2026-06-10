from ase import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np
from ase import units

metals = ['Cu', 'Ag', 'Au']
results = []
conv_fac = units.GPa / (units.eV / units.Å**3)  # eV/Å³ to GPa

for metal in metals:
    atoms = bulk(metal, 'fcc')
    cell = atoms.get_cell()
    vols, eners = [], []
    for x in np.linspace(0.95, 1.05, 7):
        scaled = atoms.copy()
        scaled.set_cell(cell * x, scale_atoms=True)
        scaled.calc = EMT()
        eners.append(scaled.get_potential_energy())
        vols.append(scaled.get_volume())
    eos = EquationOfState(vols, eners, 'birchmurnaghan')
    v0, _, B = eos.fit()
    a0 = v0 ** (1/3)
    results.append((metal, a0, B * conv_fac))

# Print comparison table
print(f"{'Metal':<4} {'Equilibrium a (Å)':<18} {'Bulk Modulus (GPa)':<18}")
print('-' * 42)
for res in results:
    print(f"{res[0]:<4} {res[1]:<18.4f} {res[2]:<18.2f}")
