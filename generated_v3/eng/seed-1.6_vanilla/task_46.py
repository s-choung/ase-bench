from ase.build import bulk, surface
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Build Pt(111) 3-layer 2x2 slab
pt_bulk = bulk('Pt', 'fcc', a=3.924)
slab = surface(pt_bulk, (111), layers=3, vacuum=10.0)
slab *= (2, 2, 1)

# Add CO to Pt top site
top_pt_idx = slab.positions[:, 2].argmax()
c_pos = slab.positions[top_pt_idx] + [0, 0, 2.0]
slab.append('C', position=c_pos)
slab.append('O', position=c_pos + [0, 0, 1.1])

# Set constraints: fix bottom Pt layer and C-O bond
bottom_z = min(slab.positions[slab.symbols == 'Pt', 2])
bottom_idxs = [i for i, at in enumerate(slab) if at.symbol == 'Pt' and abs(at.z - bottom_z) < 1e-6]
constraints = [FixAtoms(indices=bottom_idxs), FixBondLength(indices=[-2, -1])]
slab.set_constraints(constraints)

# Optimize
slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

# Print results
print(f'Final energy: {slab.get_potential_energy():.3f} eV')
print(f'C-O distance: {slab.get_distance(-2, -1):.3f} Å')
