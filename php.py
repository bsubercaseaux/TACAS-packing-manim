from eznf import modeler
import sys


N = int(sys.argv[1])
Z = modeler.Modeler()

for i in range(N+1):
    for j in range(N):
        Z.add_var(f"x_{i, j}", description=f"Element {i} is mapped to {j}")

# at least one per i 
for i in range(N+1):
    Z.add_clause([f"x_{i, j}" for j in range(N)])

# at most one per j
for j in range(N):
    Z.at_most_one([f"x_{i, j}" for i in range(N+1)])

Z.serialize(f"php-{N}.cnf")

