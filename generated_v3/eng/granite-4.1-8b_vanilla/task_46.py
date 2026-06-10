from ase import Atoms, AtomsDimer, NudgedElasticBand
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

# Create a 3-layer Pt(111) slab with periodic boundary conditions
thickness = 3
box = [(4)**0.5 * 2, (4)**0.5 * 2, thickness * 3.55]  # Lx, Ly, Lz in Å
slab = Atoms('Pt', positions=[[0, 0, i * 3.55] for i in range(thickness)],
             pbc=True, cell=box)

# Add CO molecule above the slab
co = Atoms('CO', positions=[(2, 2, thickness * 3.55 + 1.1)],
           pbc=False)

# Combine slab and CO molecule
ase_atoms = slab + co

# Fix the bottom layer of the slab
mask = [i for i, atom in enumerate(ase_atoms) if atom.position[2] < 3.55]
fix_atoms = FixAtoms(mask=mask)
ase_atoms.set_constraint(fix_atoms)

# Fix the C-O bond length
fix_bond = FixBondLength(ids=[i for i, atom in enumerate(ase_atoms) if atom.symbol in ('C', 'O')],
                         bond_length=1.13)  # Typical C-O bond length in CO
ase_atoms.set_constraint(fix_bond)

# Set up the EMT calculator
ase_atoms.set_calculator(EMT())

# Perform BFGS optimization with force convergence criterion fmax=0.05
opt = BFGS(ase_atoms, dynamics=False)
opt.run(fmax=0.05)

# Output the final energy and C-O distance
c_index = [i for i, atom in enumerate(ase_atoms) if atom.symbol == 'C'][0]
o_index = [i for i, atom in enumerate(ase_atoms) if atom.symbol == 'O'][0]
co_distance = ase_atoms.get_distance(c_index, o_index)

final_energy = ase_atoms.get_potential_energy()
print(f"Final energy: {final_energy:.4f} eV")
print(f"C-O distance: {co_distance:.3f} Å")
