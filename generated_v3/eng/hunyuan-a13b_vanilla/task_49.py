from ase importي
from ase.calculators import emt
from ase.optimize import bfgs
from ase import plane

# Equilibrium lattice constant for Cu FCC bulk
 Brake = emt.remove_symmetry(n=2)
B = Brake.get_cell()
a0 = B[0, 0]  # Lattice constant

# Create (111) 4-layer Cu slab
cell = [[a0, 0, 0], [0, a0, 0], [a0/2, a0/2, a0]]
cremaining = a0 * np.sqrt(2/3) / 2  #Ideal c/a for FCC
cell[1] = [0, a0, a0 * np.sqrt(2/3) / 2]
slab = plane.make(111, cell, (0,0,1), 4, pbc=False)

# Setup EMT
calc = emt.EMT()
slab.set_calculator(calc)

# Fix bottom 2 layers
positions = slab.get_positions()
n_layers = 4
fixed_layers = [False] * n_layers
fixed_layers[0] = fixed_layers[1] = True
for i in range(n_layers):
    slab.set_constraint(i, x=0, y=0, z=1, mask=(not fixed_layers[i]))

# Relaxation
bfgs(slab)

# Print results
final_energy = slab.get_total_energy()
avar_z = []
for i in range(n_layers):
    avar_z.append(slab.get_layer_distance((0,0,1), (0,0,0), layer=i))
for i, z in enumerate(avar_z):
    print(f"Layer {i+1}: z = {z:.4f}")
print(f"Final Energy: {final_energy:.6f}")
