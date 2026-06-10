from ase.build import bcc110

atoms = bcc110('Fe', size=(2, 2, 4), vacuum=10.0, a=2.87)
print(f"Number of atoms: {len(atoms)}")
print(f"Cell parameters (a, b, c, α, β, γ): {atoms.get_cell_lengths_and_angles()}")
