from ase import Atoms
from ase.calculators.emt import EMT
from ase.equation_of_state import EquationOfState

# Create FCC Cu structure
atoms = Atoms('Cu', positions=[(0, 0, 0)], cell=[[2, 0, 0], [0, 2, 0], [0, 0, 2]], pbc=True)
atoms.set_calculator(EMT())

# Generate volumes around equilibrium
v0 = atoms.get_volume()
volumes = []
energies = []

for scale in [0.92, 0.96, 1.0, 1.04, 1.08]:
    atoms.set_cell([v0** (1/3) * scale] * 3, scale_atoms=True)
    atoms.get_potential_energy()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

# Fit EOS and extract equilibrium properties
eos = EquationOfState(volumes, energies, 'birger')
v_eq, e_eq, B = eos.fit()

print(f'Equilibrium volume: {v_eq:.3f} Å^3')
print(f'Bulk modulus: {B:.2f} eV/Å^3')
