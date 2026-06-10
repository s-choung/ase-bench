from ase import cif
from ase.build import molecule
from ase.geometry import point_symmetry
from ase.calculators.emt import EMT
from ase.calculators.lj import Lj

try:
    # Build NaCl molecule
    na = molecule('Na', 'Cl', positions=[(0, 0, 0), (3.168, 0, 0)])
    na.cell *= 4.0
    na.set_calculator(EMT())

    # Save to CIF
    cif.write('nacif.cif', na)

    # Read back from CIF
    nacif = cif.read('nacif.cif')
    
    # Print spacegroup
    print(f"Spacegroup: {nacif.spacegroup}")

    # Print number of atoms
    print(f"Number of atoms: {len(nacif)}")

except Exception as e:
    print(f"An error occurred: {e}")
