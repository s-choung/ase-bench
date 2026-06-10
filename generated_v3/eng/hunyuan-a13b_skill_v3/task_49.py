from ase import Atoms, units
from ase.cell import Cell
from ase.build import bulk
from ase.eos import EquationOfState
from ase.calculators import EMT
from ase.optimize import BFGS
from ase.io import write

# Step 1: Find equilibrium lattice constant of Cu FCC using EOS
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()
volumes = []
energies = []
for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(a.get_cell() * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
print(f"Equilibrium lattice constant: {a.cell.lengths[0]:.4f}")

# Step 2: Create (111) 4-layer slab
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# Step 3: Attach EMT and fix bottom 2 layers
slab.calc = EMT()
bottom_layers = [atom for atom in slab if atom.position[2] < slab.cell[2, 2, 2] / 4]
slab.set_constraint(FixAtoms([atom.index for atom in bottom_layers]))

# Step 4: Run BFGS surface relaxation
BFGS(slab).run(fmax=0.05)

# Step 5: Print final energy and average z-coordinate for each layer
print(f"Final energy: {slab.get_potential_energy():.4f}")
layer_atoms = [[atom for atom in slab if abs(atom.position[2] - (i + 0.5) * slab.cell[2, 2, 2] / 4) < slab.cell[2, 2, 2] / 8] for i in range(4)]
layer_z = [sum([atom.position[2] for atom in atoms]) / len(atoms) for atoms in layer_atoms]
for i, z in enumerate(layer_z):
    print(f"Layer {i}: average z-coordinate = {z:.4f}")
