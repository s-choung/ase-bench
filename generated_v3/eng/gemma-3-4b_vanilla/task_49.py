from ase import Atoms
from ase.build import fcc111
from ase.calculators import EMT, LJ
from ase.constraints import Fix
from ase.optimize import BFGS
from ase.io import write

c = 3.615  # Cu lattice constant in Angstroms
a = 3.615
atoms = fcc111('Cu', size=(4, 4, 4), latticeconstant=a)
atoms.cell *= a
atoms.calc = EMT()
atoms.calc.kpts = (2,2,2)
atoms.add_barriers()
eos = atoms.get_equation_of_state()
lattice_constant = eos.lattice_constant
slab = fcc111('Cu', size=(4, 4, 4), latticeconstant=lattice_constant)
slab.add_atom(slab.get_positions().shape[0], [0., 0., 0.])
slab.set_pbasis([1, 0, 0], [0., 0., 0.])
slab.set_pbasis([0, 1, 0], [0., 0., 0.])
slab.set_pbasis([0, 0, 1], [0., 0., 0.])
slab.add_boundary(condition='periodic')
constraints = Fix(indices=[0, 1])
slab.set_constraint(constraints)
slab.calc = LJ()
slab.calc.sigma = 3.0
slab.calc.epsilon = 0.1
opt = BFGS(slab, trajectory='slab.traj', algo='bfgs')
opt.run(fmax=0.01)
print(f"Final energy: {slab.get_potential_energy():.6f} eV")
for i in range(4):
    print(f"Layer {i+1} average z: {sum(slab.get_positions(indices=slice(i, i+1))[0, :, 2]) / (slab.get_positions(indices=slice(i, i+1))[0].shape[0])}")
write(slab, 'slab.xyz')
