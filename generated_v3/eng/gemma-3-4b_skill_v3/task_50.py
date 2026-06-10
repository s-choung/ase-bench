import numpy as np
from ase import Atoms
from ase.build import bulk, fcc111, EMT
from ase.calculators.emt import EMT
from ase.calculators.eos import EquationOfState
from ase.visualize import view

# Copper
atoms_Cu = bulk('Cu', 'fcc', a=3.6)
atoms_Cu.calc = EMT()
eos_Cu = EquationOfState(atoms_Cu.get_volume(), atoms_Cu.get_potential_energy(), eos='birchmurnaghan')
v0_Cu, e0_Cu, B_Cu = eos_Cu.fit()
print("Cu:")
print(f"  v0: {v0_Cu}")
print(f"  e0: {e0_Cu}")
print(f"  B: {B_Cu}")
view(atoms_Cu)

# Silver
atoms_Ag = bulk('Ag', 'fcc', a=4.09)
atoms_Ag.calc = EMT()
eos_Ag = EquationOfState(atoms_Ag.get_volume(), atoms_Ag.get_potential_energy(), eos='birchmurnaghan')
v0_Ag, e0_Ag, B_Ag = eos_Ag.fit()
print("\nAg:")
print(f"  v0: {v0_Ag}")
print(f"  e0: {e0_Ag}")
print(f"  B: {B_Ag}")
view(atoms_Ag)

# Gold
atoms_Au = bulk('Au', 'fcc', a=4.07)
atoms_Au.calc = EMT()
eos_Au = EquationOfState(atoms_Au.get_volume(), atoms_Au.get_potential_energy(), eos='birchmurnaghan')
v0_Au, e0_Au, B_Au = eos_Au.fit()
print("\nAu:")
print(f"  v0: {v0_Au}")
print(f"  e0: {e0_Au}")
print(f"  B: {B_Au}")
view(atoms_Au)
