from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    # Create FCC bulk structure (conventional cell with 4 atoms)
    a0_guess = {'Cu': 3.6, 'Ag': 4.1, 'Au': 4.1}[metal]
    atoms = Atoms(metal, positions=[[0, 0, 0]], cell=[a0_guess]*3, pbc=True)
    atoms = atoms.repeat((2, 2, 2))  # 8-atom conventional cell
    
    # Set EMT calculator
    atoms.calc = EMT()
    
    # Generate volumes and energies
    volumes = []
    energies = []
    for da in np.linspace(-0.1, 0.1, 9):
        a = a0_guess + da
        atoms.set_cell([a]*3, scale_atoms=True)
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())
    
    # Fit EOS
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    a0 = (v0 * 4) ** (1/3)  # Convert volume to lattice constant (4 atoms per conventional cell)
    B_GPa = B * 160.21766208  # Convert eV/Å^3 to GPa
    
    results.append((metal, a0, B_GPa))

# Print comparison table
print(f"{'Metal':<6} {'a0 (Å)':<10} {'B (GPa)':<10}")
print("-" * 25)
for metal, a0, B in results:
    print(f"{metal:<6} {a0:<10.4f} {B:<10.2f}")
