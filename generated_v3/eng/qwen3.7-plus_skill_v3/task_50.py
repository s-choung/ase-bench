import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    atoms = bulk(metal, 'fcc', a=3.6, cubic=True)
    cell = atoms.get_cell()
    volumes, energies = [], []
    for scale in np.linspace(0.95, 1.05, 7):
        atoms_scaled = atoms.copy()
        atoms_scaled.set_cell(cell * scale, scale_atoms=True)
        atoms_scaled.calc = EMT()
        volumes.append(atoms_scaled.get_volume())
        energies.append(atoms_scaled.get_potential_energy())
    
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = v0 ** (1/3)
    results.append((metal, a0, B))

print(f"{'Metal':<8} | {'Lattice Constant (Å)':<22} | {'Bulk Modulus (eV/Å³)':<22}")
print("-" * 62)
for metal, a0, B in results:
    print(f"{metal:<8} | {a0:<22.4f} | {B:<22.4f}")
