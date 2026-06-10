from ase import Atoms
from ase.io.vasp import read_vasp, write_vasp
from ase.build import bulk

def create_and_save_cu_fcc_in_poscar():
    # Create a Copper FCC bulk structure with ASE
    cu_fcc = bulk('Cu', 'fcc', a=3.62)
    
    # Save the structure in POSCAR format
    write_vasp(cu_fcc, 'Cu_fcc_POSCAR', vasp5=True, direct=True, sort=True)

# Read back the structure from POSCAR
cu_fcc_reloaded = read_vasp('Cu_fcc_POSCAR', index='poscar', direct=True)

# Print number of atoms and cell parameters
print("Number of Atoms:", cu_fcc_reloaded.get_number_of_atoms())
print("Cell Parameters:")
print(cu_fcc_reloaded.get_cell_lengths())

create_and_save_cu_fcc_in_poscar()
