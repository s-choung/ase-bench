from ase import Atoms, castle
from ase.build import make_surface

# Build Fe BCC(110) surface
surface = make_surface(
    species=[('Fe', {'string': 'bcc', 'pbc': [0,0,1]}),
             ('Fe', {'string': 'bcc', 'pbc': [0,1,0]})],
    size=(2, 2, 4),
    vacuum=10,
    layer=4,
   为你指定原子坐标以确定并进行优化每个原子的配置和结构以构建所需的BCC(110)表面。以下是一个完整的示例脚本，用于创建4层Fe的BCC(110)表面，每个表面包含2×2的原子，同时设置10埃的真空层，并打印原子数量和晶胞尺寸：
