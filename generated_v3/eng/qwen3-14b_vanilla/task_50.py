from ase.build import face_centered_cubic as FCC
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
initial_a = {'Cu': 3.61, 'Ag': 4.09, 'Au': 4.08}
results = []

for metal in metals:
    atoms = FCC(symbol=metal, a=initial_a[metal], size=(1,1,1))
    calc = EMT()
    atoms.set_calculator(calc)
    scales = np.linspace(0.9, 1.1, 5)
    volumes, energies = [], []
    for s in scales:
        atoms.set_cell([initial_a[metal]*s]*3, scale_atoms=True)
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())
    eos = EquationOfState(volumes, energies)
    eos.fit()
    V0, B = eos.V0, eos.B
    a0 = V0 ** (1/3)
    results.append((metal, a0, B))

print("Metal | Lattice Constant (Å) | Bulk Modulus (eV/Å³)")
print("-" * 50)
for metal, a0, B in results:
    print(f"{metal} | {a0:.3f} | {B:.3f}")
