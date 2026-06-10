from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
results = {}

for metal in metals:
    atoms = bulk(metal, 'fcc', cubic=True)
    atoms.calc = EMT()
    
    cell = atoms.get_cell()
    volumes = []
    energies = []
    
    for scale in np.linspace(0.90, 1.10, 20):
        scaled = atoms.copy()
        scaled.set_cell(cell * scale, scale_atoms=True)
        scaled.calc = EMT()
        volumes.append(scaled.get_volume())
        energies.append(scaled.get_potential_energy())
    
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    
    a0 = (v0 / 4) ** (1/3) * 4 ** (1/3)
    a0 = v0 ** (1/3)
    
    a0_angstrom = (v0 / 4) ** (1/3)
    B_GPa = B / 1.60218e-19 * 1e-9 * 1e30 * 1.60218e-19 / 1e9
    
    B_GPa = B * 160.21766208
    
    results[metal] = {
        'a0': a0_angstrom,
        'B_GPa': B_GPa,
        'E0': e0
    }

print(f"\n{'='*55}")
print(f"{'Metal':<8} {'Lattice Const (Å)':<22} {'Bulk Modulus (GPa)':<20} {'E0 (eV)'}")
print(f"{'-'*55}")
for metal, res in results.items():
    print(f"{metal:<8} {res['a0']:<22.4f} {res['B_GPa']:<20.2f} {res['E0']:.4f}")
print(f"{'='*55}")
