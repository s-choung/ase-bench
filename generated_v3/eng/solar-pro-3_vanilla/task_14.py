import ase.build
from ase.atoms import Atoms

# NaCl crystal refined to lattice constant 5.64 Å
nacl = ase.build.silicon_ase()
nacl.set_cell((5.64, 5.64, 5.64))
nacl.set_atomic_numbers([11, 17])
nacl.set_positions([[0,0,0],[0.5,0.5,0.5]])

print(f"Total atoms: {nacl.get_number_of_atoms()}")
print(f"Chemical symbols: {nacl.get_chemical_symbols()}")
