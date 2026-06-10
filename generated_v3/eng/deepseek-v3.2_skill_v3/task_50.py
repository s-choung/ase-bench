import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
results = []

for symbol in metals:
    # Generate initial FCC structure
    a_guess = {'Cu': 3.6, 'Ag': 4.09, 'Au': 4.08}[symbol]
    atoms = Atoms(symbol, positions=[[0, 0, 0]], cell=[[0, a_guess/2, a_guess/2],
                                                      [a_guess/2, 0, a_guess/2],
                                                      [a_guess/2, a_guess/2, 0]],
                  pbc=True)
    atoms *= (2, 2, 2)
    
    volumes, energies = [], []
    strains = np.linspace(-0.04, 0.04, 9)
    
    for strain in strains:
        a = atoms.copy()
        a.set_cell(atoms.cell * (1 + strain), scale_atoms=True)
        a.calc = EMT()
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())
    
    eos = EquationOfState(volumes, energies)
    v0, e0, B = eos.fit()
    a0 = (4 * v0)**(1/3)
    
    results.append((symbol, a0, B / units.GPa))

print("Metal | a0 (Å) | B (GPa)")
print("-" * 25)
for symbol, a0, B in results:
    print(f"{symbol:5s} | {a0:7.3f} | {B:7.1f}")
