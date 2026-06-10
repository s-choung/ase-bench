from ase import Atoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.build import bulk, fcc111

# EOS to find equilibrium lattice constant
cu_bulk = bulk('Cu', 'fcc', a=3.6)
cu_bulk.calc = EMT()
from ase.eos import EOS
eos = EOS(cu_bulk, npoints=9)
v, e, B = eos.fit()
a_eq = (4 * v ** (1/3))

# Create (111) 4-layer slab
slab = fcc111('Cu', size=(1, 1, 4), a=a_eq, vacuum=10.0)
slab.calc = EMT()

# Fix bottom 2 layers
mask = [atom.tag > 2 for atom in slab]
fix = FixAtoms(mask=~np.array(mask))
slab.set_constraint(fix)

# Run BFGS surface relaxation
dyn = BFGS(slab)
dyn.run(fmax=0.01)

# Print final energy and average z-coordinate for each layer
print('Final energy:', slab.get_potential_energy())
for tag in range(1, 5):
    layer_z = [atom.z for atom in slab if atom.tag == tag]
    print(f'Layer {tag}: z = {sum(layer_z) / len(layer_z)}')
