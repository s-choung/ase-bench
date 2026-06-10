import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    atoms = bulk(metal, 'fcc')
    atoms.calc = EMT()
    
    cell = atoms.get_cell()
    volumes = []
    energies = []
    
    for x in np.linspace(0.95, 1.05, 7):
        new_atoms = atoms.copy()
        new_atoms.set_cell(cell * x, scale_atoms=True)
        new_atoms.get_potential_energy()
        volumes.append(new_atoms.get_volume())
        energies.append(new_atoms.get_potential_energy())
    
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = (v0)**(1/3) * 2  # fcc cubic lattice constant from primitive cell volume
    results.append((metal, a0, B))

print(f"{'Metal':<6} {'a0 (Å)':<10} {'B (eV/Å³)':<12}")
print("-" * 28)
for metal, a0, B in results:
    print(f"{metal:<6} {a0:<10.4f} {B:<12.4f}")
