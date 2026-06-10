from ase.build import bulk

# Ti HCP structure
# a = 2.95, c = 2.95 * 1.59 = 4.6905
a = 2.95
c = a * 1.59

atoms = bulk('Ti', 'hcp', a=a, c=c)

print("Cell Vectors:\n", atoms.get_cell())
print("Atomic Positions:\n", atoms.get_positions())
