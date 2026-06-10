from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB

# Initial state: third Al atom on the left
initial = Atoms('Al3',
                positions=[(0.0, 0.0, 0.0),
                           (2.0, 0.0, 0.0),
                           (8.0, 0.0, 0.0)],
                calculator=EMT())

# Final state: third Al atom on the right
final = Atoms('Al3',
              positions=[(0.0, 0.0, 0.0),
                         (6.0, 0.0, 0.0),
                         (8.0, 0.0, 0.0)],
              calculator=EMT())

# Build image list: initial + 3 intermediate + final
images = [initial]
for _ in range(3):
    img = initial.copy()
    img.calc = EMT()
    images.append(img)
images.append(final)

# Set up NEB and linearly interpolate positions
neb = NEB(images, k=0.1)
neb.interpolate()

# Print energies
for i, img in enumerate(images):
    e = img.get_potential_energy()
    print(f"Image {i}: Energy = {e:.4f} eV")
