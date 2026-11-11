# iter_nobel_nn.py
# Implementation of a Hopfield Network, the foundation of associative memory
# (2024 Nobel Prize in Physics: John Hopfield & Geoffrey Hinton).

import numpy as np

class HopfieldNetwork:
    def __init__(self, size):
        self.size = size
        self.weights = np.zeros((size, size))

    def train(self, patterns):
        """Trains the network using the Hebbian learning rule."""
        for p in patterns:
            self.weights += np.outer(p, p)
        # Set the diagonal to 0 (no self-connections)
        np.fill_diagonal(self.weights, 0)
        self.weights /= self.size

    def predict(self, state, steps=5):
        """Recovers a memory/pattern using iterative updates."""
        current_state = np.copy(state)
        print(f"Initial state: {current_state}")
        
        for step in range(steps):
            for i in range(self.size):
                # Calculate input to neuron i
                activation = np.dot(self.weights[i], current_state)
                # Step activation function (1 or -1)
                current_state[i] = 1 if activation >= 0 else -1
            
            print(f"Iteration {step + 1}: {current_state}")
            
        return current_state

if __name__ == "__main__":
    # Patterns to memorize
    # Pattern 1: [ 1,  1, -1, -1]
    # Pattern 2: [-1, -1,  1,  1]
    patterns = [
        np.array([1, 1, -1, -1]),
        np.array([-1, -1, 1, 1])
    ]
    
    net = HopfieldNetwork(size=4)
    net.train(patterns)
    
    # Corrupted/noisy state
    noisy_state = np.array([1, -1, -1, -1]) 
    
    print("--- Memory Recovery Process (Iterative) ---")
    recovered = net.predict(noisy_state)
    print(f"Final recovered state: {recovered}")