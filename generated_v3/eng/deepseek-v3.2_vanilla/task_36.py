import ase
from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

symbol = 'Ag'
structure = 'fcc'

# Initial lattice constant from EMT database
a0 = ase.data.reference_states['Ag']['a']  # ~4.09 Å for Ag

# Generate 7 lattice constants +/-5%
ratios = np.linspace(0.95, 1.05, 7)
lattice_constants = a0 * ratios

volumes = []
energies = []

for a in lattice_constants:
    atoms = Atoms(symbol, positions=[[0, 0, 0]], cell=[[0, a/2, a/2], [a/2, 0, a/2], [a/2, a/2,157;0]], pbc=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

# Fit with Birch-Murnaghan EOS
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_equilibrium = (v0 * 4)**(1/3)  # Convert volume per atom to lattice constant

print(f"Equilibrium lattice constant: {a_equilibrium:.4f} Å")
print(f"Bulk modulus: {B * 1e-3:.2f} GPa")
