from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# Setup H2 molecule
atoms = Atoms('H2', positions=[(0, 0, 0), (0, 0, 0.74)])
atoms.set_calculator(EMT())

def print_status(label):
    dist = atoms.get_distance(0, 1)
    eng = atoms.get_potential_energy()
    print(f"{label} - Bond Length: {dist:.4f} A, Energy: {eng:.4f} eV")

print_status("Before constraint")

# Apply constraint and move atoms to 0.9 A
c = FixBondLength(0, 1, 0.9)
atoms.set_constraint(c)
atoms.positions[1] = (0, 0, 0.9)

print_status("After constraint")
