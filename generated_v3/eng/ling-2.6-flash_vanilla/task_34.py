```python
from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB, IDPPRelaxingPath
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# Create FCC(111) slab with a Cu adatom
slab = make_clean_surface('Cu', size=(3, 3, 3),
                           vacuum=10.0, orthogonal=False)

# Positions: fcc hollow to hcp hollow on the surface layer
fcc_pos = slab[0].position.copy()
hcp_pos = slab[0].position.copy()
hcp_pos[0] += slab.cell[0][0] / 3 - slab.cell[0][1] / 3
hcp_pos[1] += slab.cell[1][0] / 3 - slab.cell[1][1] / 3

adatom_start = fcc_pos + [0, 0, 2.5]
adatom_end = hcp_pos + [0, 0, 2.5]

# Remove bottom two atomic layers from relaxation
indices = [i for i, atom in enumerate(slab) if atom.position[2] < 5.0]
constraint = FixAtoms(indices=indices)

# Build initial configuration with 5 NEB images
initial = slab.copy()
initial += slab[0].copy()  # add adatom at fcc hollow
initial.positions[-1] = adatom_start
images = [initial]
for i in range(1, 5):
    path = IDPPRelaxingPath(initial, slab.copy())
    images.append(path.get_image(i))

# Attach adatom to the end image
images[-1] += slab[0].copy()
images[-1].positions[-1] = adatom_end

# Set calculators and apply constraints
for img in images:
    img.set_calculator(EMT())
    img.set_constraint(constraint)

# Run NEB
neb = NEB(images)
neb.interpolate()
optimizer = BFGS(neb, trajectory='neb.traj')
optimizer.run(fmax=0.05)

# Calculate and print energy barrier
energies = [img.get_potential_energy() for img in images]
initial_energy = energies[0]
barrier = max(energies) - initial_energy
print(f'Energy barrier: {barrier:.3f} eV')
