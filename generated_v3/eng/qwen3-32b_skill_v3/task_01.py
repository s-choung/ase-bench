from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.6)
supercell = atoms * (2, 2, 2)
print("Cell (a, b, c, α, β, γ):", supercell.get_cell_lengths_and_angles())
print("Atoms:", len(supercell))
