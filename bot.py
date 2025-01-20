# from random import choice, random
# from scipy.spatial.distance import chebyshev, cityblock

# class OrthogonalBot:
# 	def __init__(self, position, board_size):
# 		self.moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 		self.board_size = board_size
# 		self.agent = position

# 	def calculate_distance(self, player, agent):
# 		return cityblock(player, agent)

# 	def find_best_move(self, player):
# 		best_distance = self.calculate_distance(player, self.agent)
# 		best_agent = None
# 		agents = []

# 		for move in self.moves:
# 			new_agent = [self.agent[0] + move[0], self.agent[1] + move[1]]
# 			if 0 <= new_agent[0] < self.board_size and 0 <= new_agent[1] < self.board_size:
# 				new_distance = self.calculate_distance(player, new_agent)
# 				if new_distance < best_distance:
# 					best_distance = new_distance
# 					best_agent = new_agent
# 				agents.append(new_agent)

# 		return best_agent if random() > 0.2 else choice(agents)

# class OctogonalBot(OrthogonalBot):
# 	def __init__(self, position, board_size):
# 		super().__init__(position, board_size)
# 		self.moves = [(-1, 0), (1, 0), (0, -1), (0, 1),
# 					  (-1, -1), (-1, 1), (1, -1), (1, 1)]

# 	def calculate_distance(self, player, agent):
# 		return chebyshev(player, agent)

import numpy as np

def orthogonal_move(agent, player):
	data = np.array([agent + player]) / 7
	actions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

	# best_action = actions[np.argmax(scores)]
	# return [agent[0] + best_action[0], agent[1] + best_action[1]]
	return actions[0]

def octogonal_move(agent, player):
	data = np.array([agent + player]) / 7
	actions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

	# best_action = actions[np.argmax(scores)]
	# return [agent[0] + best_action[0], agent[1] + best_action[1]]
	return actions[0]
