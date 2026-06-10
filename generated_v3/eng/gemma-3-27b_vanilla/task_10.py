from ase.build import fcc111, add_ideal_gas
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

def create_cu_octahedron(length):
    atoms = fcc111('Cu', size=(length, length, length), vacuum=10)
    
    mask = np.zeros(len(atoms), dtype=bool)
    for i in range(len(atoms)):
        x, y, z = atoms.positions[i]
        if abs(x) > length/2 or abs(y) > length/2 or abs(z) > length/2:
            mask[i] = True
    
    atoms = atoms[~mask]
    
    return atoms

length = 5
octahedron = create_cu_octahedron(length)

print(len(octahedron))
print(octahedron.positions.shape)
