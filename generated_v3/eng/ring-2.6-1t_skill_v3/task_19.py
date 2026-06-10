from ase import Atoms
from ase.geometry import get_distances

CO2 = Atoms('CO2',
            positions=[[0.0, 0.0, 0.0],
                       [-1.16, 0.0, 0.0],
                       [1.16, 0.0, 0.0]],
            cell=[10, 10, 10],
            pbc=False)

d, D = get_distances(0, CO2, mic=True)
for i in range(len(CO2)):
    for j in range(i + 1, len(CO2)):
        d_ij = D[i][j]
        print(f'{CO2.get_chemical_symbols()[i]}-{CO2.get_chemical_symbols()[j]}: {d_ij:.4f} Ang')
