import numpy as np
from ase.build import bulk
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

metals = ['Cu', 'Ag', 'Au']
results = []

print(f"{'Metal':<6} | {'a0 (A)':<8} | {'B (GPa)':<8}")
print("-" * 28)

for symbol in metals:
    # Initial bulk structure
    atoms = bulk(symbol, 'fcc', a=3.6)
    atoms.calc = EMT()
    
    # Initial relaxation (cell + positions)
    opt = BFGS(FrechetCellFilter(atoms))
    opt.run(fmax=0.01)
    
    initial_cell = atoms.get_cell()
    volumes = []
    energies = []
    
    # EOS scan: 5% to 105% of equilibrium volume
    for x in np.linspace(0.95, 1.05, 9):
        tmp = atoms.copy()
        tmp.set_cell(initial_cell * x, scale_atoms=True)
        tmp.calc = EMT()
        volumes.append(tmp.get_volume())
        energies.append(tmp.get_potential_energy())
    
    # EOS fitting (Birch-Murnaghan)
    eos = EquationOfState(volumes, energies)
    v0, e0, B = eos.fit()
    
    # Convert volume to lattice constant for FCC: V = a^3 / sqrt(2) -> a = (V * sqrt(2))^(1/3)
    a0 = (v0 * np.sqrt(2))**(1/3)
    
    # Convert B from eV/A^3 to GPa (1 eV/A^3 = 160.21766 GPa)
    B_gpa = B * 160.21766
    
    results.append((symbol, a0, B_gpa))
    print(f"{symbol:<6} | {a0:<8.4f} | {B_gpa:<8.2f}")
