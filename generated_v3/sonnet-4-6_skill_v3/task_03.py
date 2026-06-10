from ase.build import mx2
from ase.build import add_vacuum

slab = mx2('MoS2', kind='2H', a=3.18, thickness=3.17, vacuum=0)
add_vacuum(slab, 10)

cell = slab.get_cell()
print("Cell vectors:")
print(cell)
print("\nCell lengths and angles [a, b, c, α, β, γ]:")
params = slab.get_cell_lengths_and_angles()
print(f"a={params[0]:.4f} Å, b={params[1]:.4f} Å, c={params[2]:.4f} Å")
print(f"α={params[3]:.2f}°, β={params[4]:.2f}°, γ={params[5]:.2f}°")
