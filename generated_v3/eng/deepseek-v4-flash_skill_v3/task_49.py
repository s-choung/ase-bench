import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.eos import EquationOfState

# Step 1: Find equilibrium lattice constant of Cu FCC via EOS
atoms_ref = bulk('Cu', 'fcc', a=3.6)
cell0 = atoms_ref.get_cell()
volumes, energies = [], []
for scale in np.linspace(0.95, 1.05, 7):
    atoms = atoms_ref.copy()
    atoms.set_cell(cell0 * scale, scale_atoms=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a_eq = (v0 * 4) ** (1/3)  # FCC: 4 atoms per unit cell, volume = a^3
# Alternatively, compute directly: a_eq = (4 * v0)**(1/3)

# Step 2: Create (111) slab with 4 layers
slab = fcc111('Cu', size=(1,1,4), a=a_eq, vacuum=10.0, orthogonal=True)

# Step 3: Attach EMT calculator
slab.calc = EMT()

# Step 4: Fix bottom 2 layers (tags 0 and 1)
constraint = FixAtoms(mask=[atom.tag < 2 for atom in slab])
slab.set_constraint(constraint)

# Step 5: Relax surface
BFGS(slab).run(fmax=0.05)

# Step 6: Print final energy and average z per layer
final_energy = slab.get_potential_energy()
print(f'Final energy: {final_energy:.6f} eV')

tags = slab.get_tags()
zs = slab.positions[:, 2]
for tag in sorted(set(tags)):
    mask = tags == tag
    avg_z = zs[mask].mean()
    print(f'Layer {tag}: average z = {avg_z:.4f} Å')
