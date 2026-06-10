from ase import Atoms, units
from ase.geometry import get_distances

# Create CO2 molecule
co2 = Atoms('CO2', positions=[[0, 0, 0], 
                             [1.16, 0, 0], 
                             [-1.16, 0, 0]])
co2.set_cell((10, 10, 10))
co2.set_pbc(False)

# Calculate distances (convert to Angstrom for readability)
dist_vectors, dist_matrix = get_distances(co2.positions, cell=co2.cell, pbc=co2.pbc)

# Convert distances from Bohrs to Angstroms (ASE uses Bohr internally)
# Note: get_distances returns distances in Angstrom if cell was set in Angstrom
# But explicitly converting for clarity
dist_matrix_ang = dist_matrix / units.Bohr * units.Angstrom  # Actually, since we set cell in Ang (10,10,10), 
# but get_distances returns in the same units as cell. Since 10 is in Ang, output is in Ang. So simpler:
# dist_matrix_ang = dist_matrix  # because get_distances returns in Ang when cell is set in Ang
# However, to be explicit and avoid confusion with internal units:

# Actually, get_distances returns distances in Angstrom if the cell was set using Angstrom units (as we did)
# So we can just use:
print(f"Distance matrix (Angstrom):\n{dist_matrix}")
# Or for clarity in output:
print("\nFormatted distances (Ang):")
for i in range(len(co2)):
    for j in range(i+1, len(co2)):
        print(f"d({co2[i].symbol}-{co2[j].symbol}) = {dist_matrix[i,j]:.4f} Å")

# Alternatively, since we know the structure, we could also directly compute:
print(f"\nDirect calculation: C-O bond length = {dist_matrix[0,1]:.4f} Å")
