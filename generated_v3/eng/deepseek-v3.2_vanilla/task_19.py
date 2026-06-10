from ase import Atoms
from ase.units import Ang

atoms = Atoms('CO2', positions=[(0, 0, 0), (-1.16, 0, 0), (1.16, 0, 0)])
atoms.set_cell([10, 10, 10])
atoms.set_pbc(False)

distances = atoms.get_distances(0, [1, 2])
print(f"C-O distances: {distances[0]:.3f} Å, {distances[1]:.3f} Å")

o_o_distance = atoms.get_distance(1, 2)
print(f"O-O distance: {o_o_distance:.3f} Å")
