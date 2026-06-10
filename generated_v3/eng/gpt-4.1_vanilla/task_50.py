from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = {
    'Cu': {'symbol': 'Cu'},
    'Ag': {'symbol': 'Ag'},
    'Au': {'symbol': 'Au'}
}

results = []

for metal, params in metals.items():
    atoms = bulk(params['symbol'], 'fcc', a=4.0, cubic=True)
    atoms.calc = EMT()
    volumes = []
    energies = []
    scale_factors = np.linspace(0.94, 1.06, 7)
    a0 = atoms.cell.lengths()[0]
    for x in scale_factors:
        atoms.set_cell(np.eye(3) * a0 * x, scale_atoms=True)
        e = atoms.get_potential_energy()
        v = atoms.get_volume()
        energies.append(e)
        volumes.append(v)
    eos = EquationOfState(volumes, energies)
    v0, e0, B = eos.fit()
    a_eq = (v0 / 4)**(1/3)
    B_GPa = B / 1.60218e-19 * 1e24 / 1e9  # eV/Å³ to GPa
    results.append((metal, a_eq, B_GPa))

print(f"{'Metal':^6} | {'a₀ (Å)':^8} | {'B (GPa)':^8}")
print("-" * 28)
for metal, a_eq, B_GPa in results:
    print(f"{metal:^6} | {a_eq:8.3f} | {B_GPa:8.1f}")
