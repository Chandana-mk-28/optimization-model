# Step 0: Imports
import pulp

# Step 1: Define the problem (maximize)
problem = pulp.LpProblem("Production_Optimization", pulp.LpMaximize)

# Step 2: Decision Variables
X = pulp.LpVariable('X', lowBound=0, cat='Continuous')
Y = pulp.LpVariable('Y', lowBound=0, cat='Continuous')

# Step 3: Objective Function
problem += 3*X + 5*Y, "Total Profit"

# Step 4: Constraints
problem += 2*X + 3*Y <= 100, "Machine_Hours_Constraint"
problem += X + 2*Y <= 80,    "Labor_Hours_Constraint"

# Step 5: Solve
solution_status = problem.solve()
print("Solution Status:", pulp.LpStatus[solution_status])

# Step 6: View Results
print("Optimal Values:")
print(f"X = {X.varValue}")
print(f"Y = {Y.varValue}")
print("Max Profit =", pulp.value(problem.objective))
