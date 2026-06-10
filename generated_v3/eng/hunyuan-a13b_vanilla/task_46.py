from ase import Atom, Atoms, Molecule
from ase.io import write
from ase.constraints import FixAtoms, FixBondLength
from ase.calculator.emt import EMT
from ase.optimize import BFGS

# Setup the Pt(111) slab
platinum = {
    '-test': ['Pt', (0, 0, 0)],
    'bulk': ['Pt', (0, 0, 3)]
}
 certains = [
    [2, 3, 4], [2, 3, 5], [2, 3, 7], [2, 3, 8],  # First layer
    [7, 8, 11], [7, 8, 12], [7, 8, 14], [7, 8, 15],  # Second layer
    [14, 15, 18], [14, 15, 19], [14, 15, 21], [14, 15, 22],  # Third layer
]
bulk = Molecule('Pt', positions=[pos for symbol, pos in platinum['bulk']], cell=[6, 6, 12])
first_layer = Molecule('Pt', positions=[pos for symbol, pos in platinum['test']], cell=[6, 6, 12])
first_layer.translate((3, 3, 0))
subsystem = first_layer + bulk

# Add CO molecule
co = Molecule('CO', positions=[(1, 1, 5.5), (1, 1, 6.5)], cell=[6, 6, 12])

# Combine subsystems
system = subsystem + co
system.center()

# Define constraints
fix_bottom = FixAtoms(system, indices=[atom.index for atom in subsystem.atoms])
fix_bond = FixBondLength(system, indices=(co.atom1.idx, co.atom2.idx))

# Setup calculator and optimization
system.set_calculator(EMT())
opt = BFGS(system, fmax=0.05)
opt.maxcycle = 100

# Run optimization
opt.run()

# Output results
print('Final energy (eV):', system.get_potential_energy())
print('Final C-O distance (Å):', system.get_distance(co.atom1.idx, co.atom2.idx))
