import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here

        "*** YOUR CODE HERE ***"
        states = self.mdp.getStates()

        #run simulations
        for i in range(self.iterations):
            #make a copy of the values dictionary so that you don't change the values while running each simulation (batch version vs online version)
            stateValues = dict(self.values)
            #iterate over all states and actions
            for state in states:
                actions = self.mdp.getPossibleActions(state)
                if len(actions)>0:
                    #initialise stateValue
                    stateValue = self.computeQValueFromValues(state,actions[0])
                    for action in actions:
                        actionValue = self.computeQValueFromValues(state,action)
                        # improve if possible
                        if actionValue > stateValue:
                            stateValue = actionValue
                else:
                    stateValue= 0
                stateValues[state] = stateValue
            self.values = dict(stateValues)


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"

        Q_Value = 0
        T_States = self.mdp.getTransitionStatesAndProbs(state, action)
        #compute Q value using probability of each action occurring 
        for nextState, prob in T_States:
            Q_Value += prob * (self.mdp.getReward(state, action, nextState) + (self.discount * self.values[nextState]))

        return Q_Value

        util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """

        "*** YOUR CODE HERE ***"
        actions = self.mdp.getPossibleActions(state)

        if len(actions)>0:
            #initialise action and value variables
            bestAction = actions[0]
            bestValue = self.computeQValueFromValues(state,bestAction)
            #find action that returns best value
            for action in actions:
                actionValue = self.computeQValueFromValues(state,action)
                if actionValue > bestValue:
                    bestValue = actionValue
                    bestAction = action

            return bestAction

        else:
            return None
        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
