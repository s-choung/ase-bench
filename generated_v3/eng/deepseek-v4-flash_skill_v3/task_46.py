from ase.build import fcc111, add_adsorbate, molecule
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0, a=3.92)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

c_indices = [atom.index for atom in slab if atom.symbol == 'C']
o_indices = [atom.index for atom in slab if atom.symbol == 'O']
fix_slab = FixAtoms(mask=[a.tag >= 3 for a in slab])
fix_co = FixBondLength(c_indices[0], o_indices[0])
slab.set_constraint([fix_slab, fix_co])

slab.calc = EMT()
BFGS(slab).run(fmax=0.05)

energy = slab.get_potential_energy()
co_dist = slab.get_distance(c_indices[0], o_indices[0])
print(f"Energy: {energy:.4f} eV")
print(f"C-O distance: {co_dist:.4f} Å")
