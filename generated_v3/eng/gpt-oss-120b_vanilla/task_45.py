from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.units import Angstrom

# H2 with typical bond length ~0.74 Å
h2 = Atoms('H2', positions=[[0, 0, 0],
                            [0, 0, 0.74]],
            calculator=EMT())

def bond_len(atoms):
    return atoms.get_distance(0, 1)

# energy and bond length before constraint
e0 = h2.get_potential_energy()
b0 = bond_len(h2)
print(f'Before constraint:  bond = {b0:.3f} Å,  energy = {e0:.5f} eV')

# set new bond length to 0.9 Å and fix it
h2.set_positions([[0, 0, 0],
                  [0, 0, 0.9]])
h2.set_constraint(FixBondLength(0, 1, 0.9))

# recompute energy (geometry is now fixed at 0.9 Å)
e1 = h2.get_potential_energy()
b1 = bond_len(h2)
print(f'After constraint:   bond = {b1:.3f} Å,  energy = {e1:.5f} eV')
