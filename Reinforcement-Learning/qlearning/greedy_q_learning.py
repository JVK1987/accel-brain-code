#!/user/bin/env python
# -*- coding: utf-8 -*-
from abc import abstractproperty
from rl.q_learning import QLearning


class GreedyQLearning(QLearning):
    '''
    ε-greedy Q-Learning.

    Attributes:
        epsilon_greedy_rate:    ε-greedy rate.

    '''
    
    # ε-greedy rate.
    __epsilon_greedy_rate = 0.75
    
    def get_epsilon_greedy_rate(self):
        ''' getter '''
        if isinstance(self.__epsilon_greedy_rate, float) is True:
            return self.__epsilon_greedy_rate
        else:
            raise TypeError("The type of __epsilon_greedy_rate must be float.)

    def set_epsilon_greedy_rate(self, value):
        ''' setter '''
        if isinstance(value, float) is True:
            self.__epsilon_greedy_rate = value
        else:
            raise TypeError("The type of __epsilon_greedy_rate must be float.)

    epsilon_greedy_rate = property(get_epsilon_greedy_rate, set_epsilon_greedy_rate)

    def select_action(self, state_key, next_action_list):
        '''
        Select action by Q(state, action).
        
        Concreat method.

        ε-greedy.

        Args:
            state_key:              The key of state.
            next_action_list:       The possible action in `self.t+1`.
                                    If the length of this list is 0, all action should be possible.

        Retruns:
            The key of action.

        '''
        true_rate_list = [True] * int(self.epsilon_greedy_rate * 100)
        false_rate_list = [False] * int((1 - self.epsilon_greedy_rate) * 100)

        univerce_list = []
        [univerce_list.append(true_rate) for true_rate in true_rate_list]
        [univerce_list.append(false_rate) for false_rate in false_rate_list]

        epsilon_greedy_flag = random.choice(univerce_list)

        if epsilon_greedy_flag is True:
            # Not greedy mode.
            action_key = random.choice(next_action_list)
        else:
            # Greedy mode.
            action_key = self.predict_next_action(state_key, next_action_list)
        return action_key
