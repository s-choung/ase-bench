import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = {'Cu': 3.6, 'Ag': 4.09, 'Au': 4.08}
results = {}

for symbol, a0 in metals.items():
    atoms = bulk(symbol, 'fcc', a=a0, cubic=True)
    atoms.calc = EMT()
    
    cell = atoms.get_cell()
    volumes, energies = [], []
    
    for x in np.linspace(0.94, 1.06, 11):
        a = atoms.copy()
        a.set_cell(cell * x, scale_atoms=True)
        a.calc = EMT()
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())
    
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    
    n_atoms = len(atoms)
    a_eq = (v0 / n_atoms * 4) ** (1/3)
    B_GPa = B / 1e9 * 1.602176634e-19 / 1e-30 * 1e-9
    # B in eV/Å³ → GPa: 1 eV/Å³ = 160.2176634 GPa
    B_GPa = B * 160.2176634
    
    results[symbol] = {'a0_input': a0, 'a_eq': a_eq, 'B_GPa': B_GPa, 'e0': e0}

print(f"{'Metal':<8} {'Input a (Å)':<14} {'Eq. a (Å)':<14} {'Bulk Modulus (GPa)':<20} {'E0 (eV)':<12}")
print("-" * 70)
for symbol, r in results.items():
    print(f"{symbol:<8} {r['a0_input']:<14.3f} {r['a_eq']:<14.4f} {r['B_GPa']:<20.2f} {r['e0']:<12.4f}")
