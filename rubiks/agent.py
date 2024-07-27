import random
from Rubiks.state import State
from Rubiks.utils import move, num_solved_sides, num_pieces_correct_side, n_move_state

ALPHA = 0.6

class Agent:
    def __init__(self, QValues=None, cube=None):
        self.visited = []   #track visited states
        self.visit_count = {}  #count visits to states.
        self.revisits = 0   
        self.QV = QValues if QValues is not None else {} 
        self.R = {}      # store rewards.
    #initial state of the cube, default = cube shuffled with 6 random moves
        self.start_state = cube if cube is not None else n_move_state(n=6)
        self.curr_state = self.start_state
        self.prev_state = None
        self.second_last_action = None
        self.actions = self.start_state.actions #possible actions/moves.
    #track states at various distances (number of moves) from the current state
        self.one_away = []
        self.two_away = []
        self.three_away = []
        self.four_away = []
        self.five_away = []
        self.six_away = []
        self.last_action = None
    #count moves for each face of the cube.
        self.move = {"front": 0, "back": 0, "left": 0, "right": 0, "top": 0, "bottom": 0}

    def register_patterns(self):
    #method initializes Q-values for different states based on their distance from the solved state
        s = State()
        for action in self.actions:
            s_ = move(s, action)
            self.one_away.append(s_)
            for action_ in self.actions:
                self.QV[(s_.__hash__(), action_)] = -10 if action_ != action else 10
        for s in self.one_away:
            for action in self.actions:
                s_ = move(s, action)
                self.two_away.append(s_)
                for action_ in self.actions:
                    self.QV[(s_.__hash__(), action_)] = -6 if action_ != action else 6
        for s in self.two_away:
            for action in self.actions:
                s_ = move(s, action)
                self.three_away.append(s_)
                for action_ in self.actions:
                    self.QV[(s_.__hash__(), action_)] = -5 if action_ != action else 5
        for s in self.three_away:
            for action in self.actions:
                s_ = move(s, action)
                self.four_away.append(s_)
                for action_ in self.actions:
                    self.QV[(s_.__hash__(), action_)] = -4 if action_ != action else 4
        for s in self.four_away:
            for action in self.actions:
                s_ = move(s, action)
                self.five_away.append(s_)
                for action_ in self.actions:
                    self.QV[(s_.__hash__(), action_)] = -3 if action_ != action else 3
        for s in self.five_away:
            for action in self.actions:
                s_ = move(s, action)
                self.six_away.append(s_)
                for action_ in self.actions:
                    self.QV[(s_.__hash__(), action_)] = -1 if action_ != action else 1

    def reward(self, state, action):
        next_state = move(state, action)
        if next_state.isGoalState():
            return 100
        solved_sides = num_solved_sides(next_state) - num_solved_sides(state)
        reward = solved_sides if solved_sides > 0 else -0.1
        if (next_state.__hash__(), action) in self.QV.keys():
            reward -= 0.2
        return reward

    def max_reward(self, state, action):
        new_state = move(state, action)
        if new_state not in self.R:
            self.R[new_state] = []
            for action in self.actions:
                self.R[new_state].append(self.reward(new_state, action))
        return max(self.R[new_state])
    
    # gives a reward of 1 for each solved cube side after taking an action
