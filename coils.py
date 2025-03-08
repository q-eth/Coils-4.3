import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import mu_0

radius = 5e-2 / 2
current = 3
n_turns = 1000
length = 0.1
n = n_turns / length

B_max = mu_0 * n * current

x = np.linspace(-radius, radius, 10)
y = np.linspace(-radius, radius, 10)
z = np.linspace(-radius, radius, 10)
X, Y, Z = np.meshgrid(x, y, z)

R = np.sqrt(X**2 + Y**2 + Z**2)

B = B_max * (1 - (R / radius)**2)

B[R > radius] = 0

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

mask = R <= radius
ax.quiver(X[mask], Y[mask], Z[mask],
          np.zeros_like(X[mask]), np.zeros_like(Y[mask]), B[mask],
          length=0.1, normalize=False, color='k', alpha=0.5)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Magnetic Field in a Sphere')
ax.set_xlim([-radius, radius])
ax.set_ylim([-radius, radius])
ax.set_zlim([-radius, radius])

plt.show()

r_eff = radius * np.sqrt(0.1)
volume = (4/3) * np.pi * r_eff**3
print(f"Volume of the region where the field is 10% of the maximum: {volume:.6f} m^3")