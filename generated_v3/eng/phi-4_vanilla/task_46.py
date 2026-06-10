from ase import Atoms
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.build import surface
from ase.calculators.lj import LennardJones
from ase.calculators.emt import ElectromagneticTorque

# Define platinum (111) surface
bulk = Atoms('Pt', positions=[(0, 0, 0.1)])
pt111_slab = surface(bulk, (1, 1, 1), layers=3)

# Add CO molecule above the surface
co = Atoms('CO', positions=[(0, 0, 1.25)]
position_co = [(0.5, 0.5, 0) + (0, 0, 1.25)]
co.position = sum(position_co)
adsorbate_slab = pt111_slab + co

# Define constraints
c = FixAtoms(mask=[atom.index for atom in adsorbate_slab if atom.symbol == 'Pt'])
cl = FixBondLength(mask=[(j.index, k.index) for j in co for k in adsorbate_slab if k.symbol == 'Pt'][0], atoms=[co, adsorbate_slab[to_string_index]][1], length=1.18)

# Apply constraints
adsorbate_slab.set_constraint(c)
adsorbate_slab.set_constraint(cl)

# Calculate lattice constant from bulk
adsorbate_slab.set_cell(pt111_slab.cell, scale=1)
adsorbate_slab.center(axis=2)

# Assign calculators
adsorbate_slab.set_calculator(LennardJones())
co.set_calculator(ElectromagneticTorque())

# Optimize geometry
opt = BFGS(adsorbate_slab, trajectory='geom.js', fmax=0.05, logfile='optimize.log')
opt.run(fmax=0.05)

# Output final energy and C-O bond length
energy = opt.get_potential_energy()
co_distance = adsorbate_slab.get_distances(co, to_string_index=[adsorbate_slab.get_chemical_symbols().index('O')])[0]

print(f"Final energy: {energy}")
print(f"C-O bond length: {co_distance}")
