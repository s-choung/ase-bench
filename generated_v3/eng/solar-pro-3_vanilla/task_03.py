from ase import Atoms
from ase.visualize import view
from ase.build import bulk

# MoS2 monolayer (Mo:S = 1:2) in a 2×2 supercell
bulk_mos = bulk('MoS2', '2H', a=3.16)      # ideal lattice constant
cell = bulk_mos[::2, ::2]                  # remove every other atom -> monolayer supercell

# create monolayer
atoms = Atoms('MoS2', cell=cell.positions, cell=cell.cell,
             pbc=True)

# set atom types
atoms[atoms.index_by_symbol('Mo')] = bulk_mos.types[0]
atoms[atoms.index_by_symbol('S')] = bulk_mos.types[1]

# add 10 Å vacuum (increase z dimension)
atoms.cell[2] = atoms.cell[2] + 10.0

# print cell size
print('Cell size:', atoms.cell)

# optional pcic: EMT calculator
from ase.calculators.emt import EMT
atoms.set_calculator(EMT())
print('Energy/atom:', atoms.get_potential_energy() / len(atoms))
