im using gemini, https://share.gemini.google/d9bQLAx0QmLQ

# 第四週習題 -- 迭代法 (Week 4 Homework - Iterative Methods)

This repository contains the solutions for the Week 4 assignment on Iterative Methods, including a custom iterative problem and an implementation of the Hopfield Network (related to the 2024 Nobel Prize in Physics).

## 1. Custom Iterative Problem (`custom_iterative.py`)
In this section, I used the **Newton-Raphson Method** as a custom problem to find the square root of a number. 
This iterative method continuously updates the initial guess ($x$) using the formula:
$$x_{new} = \frac{1}{2} \left( x_{old} + \frac{n}{x_{old}} \right)$$
The loop continues until the difference between the new and old guess reaches a very small tolerance value (convergence).

## 2. Explanation of `iter_framework.py`
`iter_framework.py` acts as an abstract framework designed to simplify the writing of iterative algorithms. Generally, the core workflow of this framework can be explained in four steps:
1. **Initialization**: Accepts an initial state or guess.
2. **Termination Condition**: Uses an evaluation function to check if the iteration should stop (e.g., the difference between the current state and the previous state is less than a tolerance $\epsilon$, or a maximum number of iterations has been reached).
3. **Update Function**: Repeatedly applies transition rules to manipulate the current state into the next state.
4. **Output**: Returns the final, converged state.

By using this framework, we only need to define the *Update Function* and *Condition Function* without having to rewrite the loop structures (`while`/`for`) every time we create a new iterative algorithm.

## 3. Hopfield Network Implementation (`iter_nobel_nn.py`)
As a tribute to **John Hopfield and Geoffrey Hinton (2024 Nobel Prize in Physics Laureates)**, I implemented a basic **Hopfield Network**.
This network is an associative memory model that operates iteratively:
- **Training Phase**: Uses the Hebbian learning rule to store memory patterns inside a weights matrix.
- **Iteration Phase (Predict/Recovery)**: When given a corrupted or incomplete input (*noisy state*), the network iteratively updates the state of each neuron. As the iterations progress, the network state descends to its lowest energy (converges), successfully recovering the original memorized pattern.

### References:
- [The Nobel Prize in Physics 2024 - Geoffrey Hinton](https://www.nobelprize.org/prizes/physics/2024/hinton/facts/)
- [The Nobel Prize in Physics 2024 - John Hopfield](https://www.nobelprize.org/prizes/physics/2024/hopfield/facts/)