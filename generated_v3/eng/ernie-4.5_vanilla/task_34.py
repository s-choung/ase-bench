from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.neb import NEB
from ase.optimizers.neb import IDPP
from ase.io import read, write

# Create the FCC(111) surface and add an adatom
slab = fcc111('Cu', size=(2, 2, 2), vacuum=10.0)
adatom_pos_fcc = [1, 1, slab.cell[2, 2] / 2 + slab.cell[2, 2] * 0.2]  # Approx. fcc hollow site
adatom_pos_hcp = [0, 0, slab.cell[2, 2] / 2 + slab.cell[2, 2] * 0.2]  # Approx. hcp hollow site
slab.append(atomic_numbers=[29], positions=[adatom_pos_fcc])  # Append Cu adatom

# Label the initial (IS) and final states (FS)
initial = slab.copy()
final = slab.copy()
final[-1].position = adatom_pos_hcp  # Move adatom to hcp site

# Constrain all slab atoms except for the adatom
constraint = FixAtoms(mask=[i < len(slab) - 1 for i in range(len(slab))])
initial.set_constraint(constraint)
final.set_constraint(constraint)

# Use EMT calculator
calculator = EMT()
initial.set_calculator(calculator)
final.set_calculator(calculator)

# Create NEB with 5 images and IDPP interpolation
images = [initial.copy() for _ in range(5)]  # 5 images including initial and final
images.append(final)  # Append the final state to the images list (or use NEB directly with initial and final)
# Actually NEB takes initial and final as arguments separately, so let's adjust:
neb = NEB(images=[initial] + [img for idx, img in enumerate(images[1:-1])] + [final])  # Or simplify as below:
# Correct alternative:
images = [initial if i == 0 else initial.copy() for i in range(5)]  # Redundant but correct with clearer index
images[-1] = final
neb = NEB(images)
neb.interpolate(method='idpp')  # Use IDPP interpolation

# Optimize with NEB
optimizer = IDPP(neb, trajectory='neb_traj.traj')  # Simple NEB optimizer; you can use other optimizers as well
optimizer.run(fmax=0.01)  # Set convergence threshold

# Calculate the energy barrier
energies = [image.get_potential_energy() for image in neb.images]
energy_barrier = max(energies) - energies[0]  # Difference between max energy and initial energy
print(f"Energy barrier: {energy_barrier:.3f} eV")
