from ase.build import mx2

atoms = mx2('MoS2', kind='2H', vacuum=10)
cell = atoms.get_cell_lengths_and_angles()
print(f"Cell parameters [a, b, c, α, β, γ]: {cell} Å")
