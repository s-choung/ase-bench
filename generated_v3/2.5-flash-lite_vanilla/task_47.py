from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.neighborlist import NeighborList

atoms = fcc111('Cu', size=(3, 3, 3), vacuum=10.0)
atoms.calc = EMT()

nl = NeighborList(
    atoms.get_cell(),
    atoms.get_scaled_positions(),
    atoms.get_numbers(),
    skin=0.5,
    self_interaction=False,
    bothways=True,
    sorted_indices=False,
    use_scaled_positions=True,
    cutoff=None,
    subdomain_size=None,
    subdomain_shift=None,
    subdomain_diagonal=None,
    orbital_radius=None,
    orbital_cutoff=None,
    natural_cutoffs=True,
)

neighbor_counts = []
for i in range(len(atoms)):
    indices, offsets = nl.get_neighbors(i)
    neighbor_counts.append(len(indices))

average_coordination_number = sum(neighbor_counts) / len(atoms)
print(f"Average coordination number: {average_coordination_number}")
