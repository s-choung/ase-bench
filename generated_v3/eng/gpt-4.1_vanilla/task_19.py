from ase import Atoms

# Create CO2 molecule: C at origin, O at +/-1.16 Å along x
positions = [(0, 0, 0), (1.16, 0, 0), (-1.16, 0, 0)]
symbols = ['C', 'O', 'O']

co2 = Atoms(symbols=symbols, positions=positions, cell=[10,10,10], pbc=False)

# Print all pairwise interatomic distances
for i in range(len(co2)):
    for j in range(i+1, len(co2)):
        d = co2.get_distances(i, j)
        print(f'Distance between atom {i} ({co2[i].symbol}) and atom {j} ({co2[j].symbol}): {d[0]:.4f} Å')
