from ase import Atoms, Atom
from ase.constraints import FixAtoms, FixBondLength
from ase.io import read
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# 3‑layer Pt slab
cell = [[4.27, 0, 0], [0, 4.27, 0], [0, 0, 6.0]]   # 4.27 Å lattice constant
atoms = Atoms([
    Atom('Pt', (0, 0, 0)) if z==0 else
    Atom('Pt', (0, 0, z)) for z in range(3)
], cell=cell)
atoms.center()

# adsorb CO above Pt(111) hollow site (0.65 Å above the hollow)
CO_pos = (1.36, 1.36, 0.65)          # approximates Pt(111) hollow distance
atoms.append(Atom('C', CO_pos), align=True)
atoms.append(Atom('O', (CO_pos[0], CO_pos[1], CO_pos[2]+1.125), align=True))

# calculators
calc = EMT()
atoms.calc = calc

# constraints
cys = FixAtoms(mask=[atom.symbol == 'C' for atom in atoms])
atoms.set_constraint(cys)

ob = FixBondLength(bond=(2, 3))       # atoms indices of C and O (last two added)
atoms.set_constraint(ob)

# optimization
dyn = BFGS(atoms, trajectory='PtCO_3layer.traj')
dyn.run(fmax=0.05)

print('Final total energy (Ry):', atoms.get_potential_energy())
print('C-O distance (Å):', atoms.get_distance(2, 3))
