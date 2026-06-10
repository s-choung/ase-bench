import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

metals = {
    'Cu': 3.6,
    'Ag': 4.09,
    'Au': 4.08,
}
scales = np.linspace(0.94, 1.06, 7)

print(f'{"Metal":<5} {"a0 (Å)":>8} {"B (GPa)":>10}')
for sym, a0_guess in metals.items():
    base = bulk(sym, 'fcc', a=a0_guess)
    base.calc = EMT()
    vols, enes = [], []
    for s in scales:
        atoms = base.copy()
        atoms.set_cell(atoms.get_cell() * s, scale_atoms=True)
        vols.append(atoms.get_volume())
        enes.append(atoms.get_potential_energy())
    eos = EquationOfState(vols, enes, eos='birchmurnaghan')
    v0, _, B_eV_A3 = eos.fit()
    a0 = v0 ** (1/3)
    B_GPa = B_eV_A3 * (units.eV / units.A**3) / units.GPa
    print(f'{sym:<5} {a0:8.4f} {B_GPa:10.2f}')
