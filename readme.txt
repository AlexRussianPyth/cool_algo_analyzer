This module can analyze our algorithm and return graph of Big O for certain range of "n"

This is beta version.

Requirements:

DONE:
User can input n range, and in return there will be BigO graph for this range.

In next versions:
• User can input algorithm TYPE and n range - and in return there will be slice for this concrete type (for ex. "qubic")
• Button for usual graph with computation "zones"

1 Constants
log(n) Logarithmic
n linear
nlog(n) Log linear
n**2 quadratic
n**3 qubic
2**n exponential
n! Factorial

Development Log:

24.04.2021
When the "n" grows, we can't directly brutforce our graph, because needed computational power doesn't compare with my shitty processor.

It means that we can't directly work with every "n" in range, and for computational economy purposes we will 
use NumPy linspace function, and if our "n" range will be too big - we will construct only one n in 20, or 50
