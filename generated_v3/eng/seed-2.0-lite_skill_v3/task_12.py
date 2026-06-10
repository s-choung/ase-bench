from ase.build import bulk

# Create HCP Ti bulk with specified lattice parameters
a = 2.95
c = a * 1.59  # c/a = 1.59
ti_bulk = bulk('Ti', 'hcp', a=a, c=c)

# Print required output
print("Cell vectors (Å):")
print(ti_bulk.get_cell())
print("\nAtomic positions (Å):")
print(ti_bulk.get_positions())
