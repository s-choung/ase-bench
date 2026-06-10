from ase import Atoms, Atom, units
from ase.build import bulk, fcc111, add_adsorbate
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.eos import EquationOfState
import numpy as np

# Step 1: Find equilibrium lattice constant using EOS
cu_bulk = bulk('Cu', 'fcc', cubic=True)
cu_bulk.set_calculator(EMT())

volumes = []
energies = []

for x in np.linspace(0.7, 1.3, 7):  # Sweep over different lattice constants
    test_bulk = cu_bulk.copy()
    test_bulk.set_cell(test_bulk.get_cell() * x, scale_atoms=True)
    test_bulk.set_calculator(EMT())
    volumes.append(test_bulk.get_volume())
    energies.append(test_bulk.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
equilibrium_lattice = (v0 / cu_bulk.get_volume()) ** (1/3) * cu_bulk.get_cell()[0, 0]

# Step 2: Create a (111) 4-layer slab with equilibrium lattice constant
slab = fcc111('Cu', size=(3, 3, 4), a=equilibrium_lattice, vacuum=10)
slab.set_calculator(EMT())

# Step 3: Fix the bottom 2 layers
cutoff = np.mean(np.linalg.norm(slab.get_cell()[2]))
fixed_layers = [
    Atoms(),
    Atoms(),
    Atoms(list((atom.index for atom in slab if atom.position[2] < (1 * cutoff))),
          cell=slab.get_cell(), pbc=slab.get_pbc())
]
slab.set_constraint(FixAtoms(mask=[any(a in layer for layer in fixed_layers) for a in slab]))

# Step 4: Run BFGS surface relaxation
optimizer = BFGS(slab)
optimizer.run(fmax=0.05)

# Step 5: Calculate and print the final energy and average z-coordinate for each layer
final_energy = slab.get_potential_energy()
print(f"Final Energy: {final_energy} eV")

layers = 4
layer_height = slab.get_cell()[2, 2] / layers
atoms_sorted = sorted(
    slab,
    key=lambda atom: atom.position[2]
)
layer_averages_z = []

for i in range(layers):
    layer = atoms_sorted[
        int(i * slab.get_number_of_atoms() / layers):int((i + 1) * slab.get_number_of_atoms() / layers)
    ]
    avg_z = np.mean([atom.position[2] for atom in layer])
    layer_averages_z.append(avg_z)
    print(f"Layer {i + 1} average z: {avg_z:.4f} Angstroms")
