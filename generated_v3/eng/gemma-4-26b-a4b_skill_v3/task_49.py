import numpy as np
from ase import units
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.eos import EquationOfState

# 1. Find equilibrium lattice constant via EOS
cu_bulk = bulk('Cu', 'fcc', a=3.5)
cu_bulk.calc = EMT()
volumes, energies = [], []
cell_orig = cu_bulk.get_cell()

for x in np.linspace(0.9, 1.1, 11):
    temp_atoms = cu_bulk.copy()
    temp_atoms.set_cell(cell_orig * x, scale_atoms=True)
    temp_atoms.calc = EMT()
    volumes.append(temp_atoms.get_volume())
    energies.append(temp_atoms.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a_eq = (v0 * 3**(-2/3))**0.5 # simplified for FCC
cu_bulk.set_cell(cu_bulk.get_cell() * (a_eq/3.5), scale_atoms=True)

# 2. Create 4-layer FCC(111) slab
slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0, a=a_eq)
slab.calc = EMT()

# 3. Fix bottom 2 layers (indices 0 and 1 in z-direction)
# Determine indices by sorting z-coordinates
z_coords = slab.positions[:, 2]
layer_indices = np.argsort(z_coords)
# In a 4-layer slab, indices are roughly distributed; we find the first two layers
bottom_indices = layer_indices[:len(layer_indices)//4 * 2] 
slab.set_constraint(FixAtoms(indices=bottom_indices))

# 4. Relax surface (top layers)
opt = BFGS(slab)
opt.run(fmax=0.05)

# 5. Output results
print(f"Final Energy: {slab.get_potential_energy():.4f} eV")
# Calculate average z for each of the 4 layers
z_pos = slab.positions[:, 2]
# Since it's a structured slab, we group by the original layer index logic
# But for a simple script, we'll just group atoms by quantized z-levels
unique_zs = np.unique(np.round(z_pos, decimals=1))
for i, z in enumerate(unique_zs):
    layer_atoms = slab[np.abs(z_pos - z) < 0.5]
    print(f"Layer {i} avg z: {layer_atoms.get_center_of_mass()[2]:.4f}")
