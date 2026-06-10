from ase.build import bulk, bulk_from_atoms
from ase.geometry import primitive_cell
from ase.utils import makedirs
from ase.io import write
import numpy as np

def create_octahedron(length):
    # Create a simple cubic cell
    a = np.array([[length, 0, 0], 
                  [0, length, 0], 
                  [0, 0, length]], dtype=float)
    
    # Create a simple cubic structure
    atoms = bulk('Cu', 'fcc', a=a, cubic=True)
    
    # Adjust positions to form an octahedron
    positions = atoms.get_positions()
    center = np.mean(positions, axis=0)
    
    # Filter to get only the octahedral shape
    octahedron_positions = []
    for pos in positions:
        if np.allclose(pos[2] - center[2], np.abs(pos[0] - center[0]), atol=1e-2):
            octahedron_positions.append(pos)
    
    # Make new Atoms object
    octahedron_atoms = atoms.__class__((len(octahedron_positions),), positions=octahedron_positions)
    
    # Obtain primitive cell
    pcell = primitive_cell(octahedron_atoms)
    pcell.set_pbc([False, False, False])
    
    return pcell

# Define the length of the octahedron
length = 5

# Create the octahedron
octahedron = create_octahedron(length)

# Print the number of atoms and their positions' shape
print(f"Number of atoms: {len(octahedron)}")
print(f"Positions shape: {octahedron.get_positions().shape}")
