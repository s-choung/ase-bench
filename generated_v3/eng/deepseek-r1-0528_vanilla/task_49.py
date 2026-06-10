from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.eos import EquationOfState

# Step 1: Find bulk FCC Cu equilibrium lattice constant using EOS
a_guess = 3.6
cu_bulk = bulk('Cu', 'fcc', a=a_guess)
cu_bulk.calc = EMT()
volumes = [a**3 for a in [a_guess * (1 - 0.05), a_guess, a_guess * (1 + 0.05)]]
energies = []
for vol in volumes:
    a = vol**(1/3)
    cu_bulk.set_cell([[a, 0, 0], [0, a, 0], [0, 0, a]], scale_atoms=True)
    energies.append(cu_bulk.get_potential_energy())
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a0 = v0**(1/3)

# Step 2: Create a 4-layer slab with that lattice constant
slab = fcc111('Cu', (1, 1, 4), a=a0, vacuum=7.0)
slab.calc = EMT()

# Step 3: Fix bottom 2 layers and relax
bottom_layer = [atom.index for atom in slab if atom.position[2] < slab.positions[:, 2].min() + 4.0]
slab.set_constraint(FixAtoms(indices=bottom_layer))
opt = BFGS(slab)
opt.run(fmax=0.05)

# Step 4: Print energy and average z-coordinate per layer
print("Final Energy:", slab.get_potential_energy())
z_positions = slab.get_positions()[:, 2]
z_min, z_max = z_positions.min(), z_positions.max()
layer_height = (z_max - z_min) / 4
for i in range(4):
    layer_atoms = [z for z in z_positions if z_min + i*layer_height <= z < z_min + (i+1)*layer_height]
    print(f"Layer {i+1} Avg Z: {sum(layer_atoms)/len(layer_atoms):.6f}")
