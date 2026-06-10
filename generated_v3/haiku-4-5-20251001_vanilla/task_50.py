from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
results = {}

for metal in metals:
    atoms = bulk(metal, 'fcc', a=4.0)
    atoms.calc = EMT()
    
    cell_params = np.linspace(0.95, 1.05, 5)
    energies = []
    volumes = []
    
    for scale in cell_params:
        atoms_scaled = atoms.copy()
        atoms_scaled.set_cell(atoms.cell * scale, scale_atoms=True)
        atoms_scaled.calc = EMT()
        energies.append(atoms_scaled.get_potential_energy())
        volumes.append(atoms_scaled.get_volume())
    
    eos = EquationOfState(volumes, energies)
    v0, e0, B = eos.fit()
    
    a0 = (v0 * 4) ** (1/3)
    B_GPa = B / 1.602e-19 * 1e-9
    
    results[metal] = {'a0': a0, 'B': B_GPa}

print("\n" + "="*60)
print(f"{'Metal':<10} {'Lattice Constant (Å)':<25} {'Bulk Modulus (GPa)':<25}")
print("="*60)
for metal in metals:
    print(f"{metal:<10} {results[metal]['a0']:<25.4f} {results[metal]['B']:<25.2f}")
print("="*60 + "\n")
