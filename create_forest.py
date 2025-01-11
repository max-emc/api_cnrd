import numpy.random as npr
from pyquaternion import Quaternion
from scipy.stats import qmc

class ForestGenerator:

	def __init__(self, density, radius, tile_size, trees):
		self.density = density
		self.radius = radius
		self.tile_size = tile_size
		self.trees = trees

		self.sizes = self.generate_sizes()
		self.angles = self.generate_quaternions()
		self.species = self.generate_species()
		self.positions = self.generate_positions()


	def generate_sizes(self):
		sizes = npr.lognormal(
			mean=0,
			sigma=0.3,
			size=self.density
		)

		return sizes

	def generate_quaternions(self):
		quaternions = []

		for _ in range(self.density):
			angle_x = npr.uniform(-10, 10)
			angle_y = npr.uniform(0, 360)
			angle_z = npr.uniform(-10, 10)

			q_x = Quaternion(axis=[1, 0, 0], degrees_angle=angle_x)
			q_y = Quaternion(axis=[0, 1, 0], degrees_angle=angle_y)
			q_z = Quaternion(axis=[0, 0, 1], degrees_angle=angle_z)
			q = q_x * q_y * q_z

			quaternions.append({"w": q.w, "x": q.x, "y": q.y, "z": q.z})

		return quaternions

	def generate_species(self):
		return npr.choice(self.trees, size=self.density)

	def generate_positions(self):
		engine = qmc.PoissonDisk(d=2, radius=self.radius)
		positions = engine.random(self.density) * self.tile_size
		return positions


	def create_forest(self):
		data = [{
			"x": pos[0],
			"z": pos[1],
			"size": size,
			"angle": angle,
			"specie": specie
		}
		for pos, size, angle, specie, in zip(
				self.positions, self.sizes, self.angles, self.species
			)
		]

		return data

if __name__ == "__main__":
	forest = ForestGenerator(30, 0.11, 3, ["A", "B", "C"])
	data = forest.create_forest()

	import numpy as np

	sizes = forest.sizes

	[print(s) for s in sizes]
