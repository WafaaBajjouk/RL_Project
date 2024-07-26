# Rubiks/agent.py

import random
from Rubiks.state import State
from Rubiks.utils import move, num_solved_sides, num_pieces_correct_side, n_move_state

ALPHA = 0.6

class Agent:
    def __init__(self, QValues=None, cube=None):
        self.visited = []
        self.visit_count = {}
        self.revisits = 0
        self.QV = QValues if QValues is not None else {}
        self.R = {}
        self.start_state = cube if cube is not None else n_move_state(n=6)
        self.curr_state = self.start_state
        self.prev_state = None
        self.second_last_action = None
        self.actions = self.start_state.actions
        self.one_away = []
        self.two_away = []
        self.three_away = []
        self.four_away = []
        self.five_away = []
        self.six_away = []
        self.last_action = None
        self.move = {"front": 0, "back": 0, "left": 0, "right": 0, "top": 0, "bottom": 0}

    def register_patterns(self):
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
        reward = -0.1
        solved_sides = 2 * (num_solved_sides(next_state) < num_solved_sides(state))
        solved_pieces = 0.5 * (num_pieces_correct_side(next_state) < num_pieces_correct_side(state))
        if (next_state.__hash__(), action) in self.QV.keys():
            reward -= 0.2
        reward -= solved_sides
        reward -= solved_pieces
        return reward

    def max_reward(self, state, action):
        new_state = move(state, action)
        if not new_state in self.R.keys():
            self.R[new_state] = []
            for action in self.actions:
                self.R[new_state].append(self.reward(new_state, action))
        return max(self.R[new_state])
