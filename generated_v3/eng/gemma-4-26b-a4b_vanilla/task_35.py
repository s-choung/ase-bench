import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.geometry import distance

# Define fixed atoms (Al-like positions, though EMT is for Cu/Ag/Au/Ni/Pd/Pt)
# Using EMT, we'll treat these as generic atoms for the sake of the demonstration
fixed_a = np.array([0.0, 0.0, 0.0])
fixed_b = np.array([4.0, 0.0, 0.0])
moving_start = np.array([1.0, 1.0, 0.0])
moving_end = np.array([3.0, -1.0, 0.0])

def create_state(moving_pos):
    atoms = Atoms('Al3', positions=[fixed_a, fixed_b, moving_pos])
    atoms.calc = EMT()
    return atoms

# Initial and Final states
initial = create_state(moving_start)
final = create_state(moving_end)

# Create 3 images (including start/end logic in NEB)
# NEB requires the list of images. We interpolate the moving atom.
images = []
n_images = 3
for i in range(n_images):
    # Linear interpolation of the 3rd atom's position
    frac = i / (n_images - 1)
    pos = moving_start + frac * (moving_end - moving_start)
    img = create_state(pos)
    images.append(img)

# Perform NEB
neb = NEB(images)
neb.interpolate() # Interpolates the internal images if not already done, 
                  # but here we manually set them via the list.

# For a real calculation, one would call neb.run()
# Here we just print the energies of the provided images as requested
print(f"{'Image':<10} {'Energy (eV)':<15}")
for i, img in enumerate(images):
    print(f"{i:<10} {img.get_potential_energy():<15.6f}")
