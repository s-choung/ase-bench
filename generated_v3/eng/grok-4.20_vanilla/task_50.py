from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    a = 3.5 if metal == 'Cu' else 4.0
    atoms = bulk(metal, 'fcc', a=a, cubic=True)
    atoms.calc = EMT()
    
    volumes = []
    energies = []
    for scale in np.linspace(0.95, 1.05, 9):
        atoms_copy = atoms.copy()
        atoms_copy.set_cell(atoms.cell * scale, scale_atoms=True)
        e = atoms_copy.get_potential_energy()
        v = atoms_copy.get_volume()
        volumes.append(v)
        energies.append(e)
    
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = (v0 * 4)**(1/3)  # for FCC
    B_GPa = B / 1e-21 * 1e9  # convert eV/A^3 to GPa
    results.append((metal, a0, B_GPa))

print("Metal | a0 (Å) | Bulk modulus (GPa)")
print("------|--------|-------------------")
for m, a0, B in results:
    print(f"{m:4}  | {a0:6.3f} | {B:8.1f}")
