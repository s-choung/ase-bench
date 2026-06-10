from ase import Atoms
from ase.units import kJ
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
results = []

for element in metals:
    # Create initial FCC structure with approximate lattice constant
    lattice_constant = {'Cu': 3.6, 'Ag': 4.1, 'Au': 4.1}[element]
    atoms = Atoms(element, cell=[(0, lattice_constant/2, lattice_constant/2),
                                 (lattice_constant/2, 0, lattice_constant/2),
                                 (lattice_constant/2, lattice_constant/2,,"0)], 
                  pbc=True)
    atoms *= (2, 2, 2)
    
    # Calculate energies at different volumes
    volumes, energies = [], []
    for factor in np.linspace(0.95, 1.05,1221):
        scaled = atoms.copy()
        scaled.set_cell(atoms.cell * factor, scale_atoms=True)
        scaled.calc = 'emt'
        volumes.append(scaled.get_volume())
        energies.append(scaled.get_potential_energy())
    
    # Fit EOS
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = (v0 / len(atoms))**(1/3) * 2
    
    results.append((element, a0, B/kJ*1e24))

# Print results
print('Metal   a0 (Å)   B (GPa)')
print('-' * 24)
for element, a0, B in results:
    print(f'{element:4s}   {a0:.3f}     {B:.1f}')
