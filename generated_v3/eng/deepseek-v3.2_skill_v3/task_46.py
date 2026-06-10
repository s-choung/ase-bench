from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0, a=3.92)
co = molecule('CO')
add_adsorbate(slab, co, height=1.5, position='ontop')

bottom_mask = [atom.index for atom in slab if atom.tag >= 2]
bottom_constraint = FixAtoms(indices=bottom_mask)

c_index = [atom.index for atom in slab if atom.symbol == 'C'][0]
o_index = [atom.index for atom in slab if atom.symbol == 'O'][0]
bond_constraint = FixBondLength(c_index, o_index)

slab.set_constraint([bottom_constraint, bond_constraint])
slab.calc = EMT()

opt = BFGS(slab, trajectory='opt.traj')
opt.run(fmax=0.05)

energy = slab.get_potential_energy()
distance = slab.get_distance(c_index, o_index)

print(f'Final energy: {energy:.3f} eV')
print(f'C-O distance: {distance:.3f} Å')
