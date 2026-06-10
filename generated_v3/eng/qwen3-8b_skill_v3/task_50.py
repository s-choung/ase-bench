import numpy as np
from ase import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
results = {}

for metal in metals:
    atoms = bulk(metal, 'fcc')
    atoms.calc = EMT()
    scales = np.linspace(0.95, 1.05, 7)
    volumes, energies = [], []
    for scale in scales:
        a = atoms.copy()
        a.set_cell(atoms.get_cell() * scale, scale_atoms=True)
        a.calc = EMT()
        a.get_potential_energy()
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = v0 ** (1/3)
    B_GPa = B * 160.2176634
    results[metal] = (a0, B_GPa)

print("Metal | a0 (Å) | B (GPa)")
print("---|---|---")
for metal, (a0, B) in results.items():
    print(f"{metal} | {a0:.5f} | {B:.2f}")
