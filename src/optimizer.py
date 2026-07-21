from pulp import LpMaximize
from pulp import LpProblem
from pulp import LpVariable
from pulp import lpSum
from pulp import LpStatus
from pulp import value


def solve_optimization(
    workers,
    budget,
    profit_per_unit,
    labor_cost,
    max_units
):
    """
    Simple linear optimization model.
    """

    model = LpProblem(
        name="Operational_Optimization",
        sense=LpMaximize
    )

    production = LpVariable(
        name="production",
        lowBound=0,
        cat="Integer"
    )

    model += (
        profit_per_unit * production,
        "Total_Profit"
    )

    model += (
        labor_cost * production <= budget,
        "Budget"
    )

    model += (
        production <= workers * max_units,
        "Capacity"
    )

    model.solve()

    return {
        "status": LpStatus[model.status],
        "production": int(value(production)),
        "profit": round(value(model.objective), 2)
    }