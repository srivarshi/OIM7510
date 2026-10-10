# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
# ]
# ///
"""Mini Project 1.
"""

import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium", sql_output="polars")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A Reorder Simulation#
    A coffee shop near campus goes through eight to 20 cartons of oat milk a day. Its distributor delivers in lots of 100 cartons, three days after the order is placed. When the shop runs out, customers who wanted oat milk walk out, and when it orders too early, cartons sit in a small refrigerator it needs for other things. The owner wants to know how low stock should fall before the next order goes in.

    starting_stock = 60
    order_quantity = 100
    lead_time_days = 3
    reorder_points = [20, 30, 40, 50]
    daily_demand = [12, 15, 9, 14, 18, 11, 10, 16, 13, 17, 8, 12, 20, 14, 11,
                    9, 15, 13, 16, 12, 10, 14, 19, 11, 13, 15, 9, 12, 17, 14]
    Copy
    The rules for one day

    Any delivery due today arrives first.
    Sell up to today's demand. Demand you cannot meet is lost.
    At the end of the day, add the stock on hand to everything already ordered and not yet delivered. If that total is at or below the reorder point, place an order. An order placed at the end of day 2 arrives at the start of day 5.
    The main task

    A table with one row per day for a reorder point of 40: day, starting stock, arrived, demand, sold, lost, ending stock, and units ordered.
    The same simulation for every reorder point in the list, compared in one table: units lost, days with a lost sale, orders placed, and average ending stock over the 30 days.
    One sentence recommending a reorder point, with the numbers that justify it.
    You may need a loop inside a loop, or a function written with def, to run the same simulation for each reorder point.

    Going further

    Put a cost on each part: $0.50 a carton for each night in the refrigerator, $40 delivery fee for each order, $8 of lost margin for each carton the shop could not sell. Which reorder point from 10 to 80 costs least?
    Generate a year of random demand with a fixed seed, and find out whether your recommendation still holds.
    Make the order quantity a second input and search both together.
    Add a slider for the reorder point, so the owner can try one, and a chart of stock over the 30 days.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Mini Project 1

    Your choice of option, what each one asks for, the due date and how it is graded are on the Mini Project 1 page of the course site, linked from the calendar. This notebook is the shape to build it in. Keep the headings, and replace each line in italics with your own.

    Save it in your course repository as `projects/mp1/<your-tool>.py`, named for what it does, such as `loan-schedule.py`, and open it with `uv run marimo edit`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. The Question

    *Who would use this, and what decision does it help them make? Two or three sentences, in words somebody outside this course would understand.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A coffee shop owner or employee would use to deternmine when to order the oat milk, so they donot run out of it and also donot have overstock.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. My Plan Before AI

    *Before you ask your agent anything, write how you would solve it: the steps, in order, in plain words, in five lines or more. Then answer these two questions:*

    - *What does your loop carry from one step to the next, the way a running total carries its sum?*
    - *Which check will you use in section 6, and which two numbers should agree?*

    *Commit this notebook with the message `mp1: plan before AI`.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Step 1 - Check for deliveries - At the start of each day, check if any order placed 3 days ago has arrived and add those cartons to the current stock
    Step 2 - Handle daily Sales - Subtract todays customer demand from our current inventory. If demand is higher than stock, we sell everything we have left
    Step 3 - Ending Stock - Determine how many cartons are left in the refrigerator at the end of the day
    Step 4 - Track any incoming order from the pervious day
    Step 5 - Evaluate reorder - at the end of the day, add ending stock and all incoming orders together. If the total is at or below the reorder point, place a new order for 100 cartons.
    Step 6 - Repeat this same process for 30 days
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. Inputs

    Every number the project starts from goes in the cell below, and nowhere else, so that changing one input changes every result after it.

    Copy in the default inputs for your option from the Mini Project 1 page. If you chose D, your own option, type your data in here, or ask your agent to generate it with `faker`. The required part reads no file.
    """)
    return


@app.cell
def _():
    # Your inputs.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. The Work

    Add as many cells as you need. Try each step yourself before you ask your agent, and commit as you go.
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5. The Answer

    *A table of your results in the cell below, printed with `print` and f-strings, then one sentence here that answers the question in section 1, with the number in it.*
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 6. How I Know These Numbers Are Right

    *At least one check that reaches a result a second, independent way. Name what you compared and what came out.*
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 7. Working With the Agent

    *Pick one piece of AI output you did not accept as-is. What did it give you, what did you change, and how did you know? Point to the commit or the cell.*

    *If the agent got it right the first time: what did you do to verify that?*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 8. Going Further

    *Take at least one step past the main task, in any direction, and use your agent as much as you like. It does not have to work. State what you tried, what you found, and where it is in this notebook.*
    """)
    return


if __name__ == "__main__":
    app.run()
