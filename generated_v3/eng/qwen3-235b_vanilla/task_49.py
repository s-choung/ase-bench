from ase import Atoms, Atom
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.build import bulk, fcc111
from ase.constraints import FixAtoms
from ase.optimize import BFGS

# Find equilibrium lattice constant for Cu FCC using EMT
atoms_bulk = bulk('Cu', 'fcc', a=3.6)
cell = atoms_bulk.get_cell()

# Generate volume-energy points
volumes = []
energies = []
for a in [3.4, 3.5, 3.6, 3.7, 3.8]:
    atoms_bulk.set_cell([cell[0], cell[1], [0, 0, a]], scale_atoms=True)
    atoms_bulk.calc = EMT()
    volumes.append(atoms_bulk.get_volume())
    energies.append(atoms_bulk.get_potential_energy())

# Fit EOS
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a_eq = (v0 * 4)**(1/3)  # Convert FCC volume back to lattice constant

# Create 4-layer Cu(111) slab
slab = fcc111('Cu', size=(1, 1, 4), a=a_eq, vacuum=10.0)

# Fix bottom 2 layers
mask = [atom.tag >= 3 for atom in slab]
constraint = FixAtoms(mask=mask)
slab.set_constraint(constraint)

# Attach EMT and relax
slab.calc = EMT()
opt = BFGS(slab, trajectory=None)
opt.run(fmax=0.01)

# Output final energy and average z per layer
print("Final energy:", slab.get_potential_energy())
z_positions = [(atom.position[2], atom.tag) for atom in slab]
for layer in range(1, 5):
    layer_z = [z for z, tag in z_positions if tag == layer]
    print(f"Layer {layer} average z:", sum(layer_z) / len(layer_z))
