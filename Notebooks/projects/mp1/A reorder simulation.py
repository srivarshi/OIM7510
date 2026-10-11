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
    def _():
        # Your inputs.
        starting_stock = 60
        order_quantity = 100
        lead_time_days = 3
        reorder_points = [20, 30, 40, 50]
        daily_demand = [12, 15, 9, 14, 18, 11, 10, 16, 13, 17, 8, 12, 20, 14, 11,
                        9, 15, 13, 16, 12, 10, 14, 19, 11, 13, 15, 9, 12, 17, 14]
        return


    _()
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
    starting_stock = 60
    order_quantity = 100
    lead_time_days = 3
    reorder_points = [20, 30, 40, 50]
    daily_demand = [12, 15, 9, 14, 18, 11, 10, 16, 13, 17, 8, 12, 20, 14, 11,
                    9, 15, 13, 16, 12, 10, 14, 19, 11, 13, 15, 9, 12, 17, 14]

    def simulate(reorder_point):

        stock = starting_stock
        orders = []

        results = []

        for day in range(1, 31):

            # 1. Check if an order arrives today
            arrived = 0
            for order in orders:
                if order["arrival_day"] == day:
                    arrived = arrived + order["quantity"]
            stock = stock + arrived

            # Starting stock after today's delivery arrives
            start_stock = stock

            # 2. Get today's demand

            demand = daily_demand[day - 1]

            # 3. Sell as much as possible

            if stock >= demand:
                sold = demand
                lost = 0
            else:
                sold = stock
                lost = demand - stock
            stock = stock - sold
            ending_stock = stock

            # 4. Calculate stock already ordered but not delivered

            outstanding = 0
            for order in orders:
                if order["arrival_day"] > day:
                    outstanding = outstanding + order["quantity"]

            # 5. Decide whether to place a new order

            units_ordered = 0
            inventory_position = ending_stock + outstanding
            if inventory_position <= reorder_point:
                units_ordered = order_quantity
                new_order = {
                    "arrival_day": day + lead_time_days,
                    "quantity": order_quantity
                }
                orders.append(new_order)

            # 6. Save today's results
            results.append({
                "day": day,
                "starting_stock": start_stock,
                "arrived": arrived,
                "demand": demand,
                "sold": sold,
                "lost": lost,
                "ending_stock": ending_stock,
                "units_ordered": units_ordered
            })
        return results

    return reorder_points, simulate


@app.cell
def _(simulate):
    results = simulate(40)

    print("Day | Start | Arrived | Demand | Sold | Lost | Ending | Ordered")

    for row in results:

        print(row)
    return


@app.cell
def _(reorder_points, simulate):
    def _():
        print("Reorder | Units Lost | Lost Days | Orders | Avg Ending Stock")
        for reorder_point in reorder_points:
            results = simulate(reorder_point)
            units_lost = 0
            lost_days = 0
            orders_placed = 0
            total_ending_stock = 0
            for row in results:
                # Add lost units
                units_lost = units_lost + row["lost"]
                # Count days with lost sales
                if row["lost"] > 0:
                    lost_days = lost_days + 1
                # Count orders placed
                if row["units_ordered"] > 0:
                    orders_placed = orders_placed + 1
                # Add ending stock
                total_ending_stock = total_ending_stock + row["ending_stock"]
            # Calculate average ending stock
            average_stock = total_ending_stock / 30
        return print(
                reorder_point,
                "|", units_lost,
                "|", lost_days,
                "|", orders_placed,
                "|", round(average_stock, 2)
            )
    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5. The Answer

    *A table of your results in the cell below, printed with `print` and f-strings, then one sentence here that answers the question in section 1, with the number in it.*
    """)
    return


@app.cell
def _(reorder_points, simulate):
    def _():
        print(f"{'Reorder Point':<15} {'Units Lost':<12} {'Lost Days':<12} {'Orders':<10} {'Avg Stock':<12}")
        for reorder_point in reorder_points:
            results = simulate(reorder_point)
            units_lost = 0
            lost_days = 0
            orders_placed = 0
            total_ending_stock = 0
            for row in results:
                units_lost += row["lost"]
                if row["lost"] > 0:
                    lost_days += 1
                if row["units_ordered"] > 0:
                    orders_placed += 1
                total_ending_stock += row["ending_stock"]
            average_stock = total_ending_stock / 30
        return print(f"{reorder_point:<15} {units_lost:<12} {lost_days:<12} {orders_placed:<10} {average_stock:<12.2f}")
    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 6. How I Know These Numbers Are Right

    *At least one check that reaches a result a second, independent way. Name what you compared and what came out.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    I manually checked the first few days for the reorder point of 40. The shop starts with 60 cartons, and after demands of 12 and 15 on Days 1 and 2, it has 33 cartons left (60 − 12 − 15 = 33). Since 33 is below the reorder point of 40, the simulation correctly places an order for 100 cartons at the end of Day 2. With a 3-day lead time, the order arrives at the start of Day 5, which matches the output.
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
    One piece of AI output I did not accept as-is was the code for comparing the different reorder points. The AI initially gave me code that used row[5], row[6], and row[7] to access the simulation results. When I ran the code, I received a KeyError: 5. I checked my simulation function and saw that each day’s results were stored as a dictionary with keys such as "lost", "ending_stock", and "units_ordered", rather than as a list. I changed the code to use row["lost"], row["ending_stock"], and row["units_ordered"]. After making this change, the comparison ran successfully and produced results for all four reorder points. This correction can be seen in the cell where I compare reorder points 20, 30, 40, and 50.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 8. Going Further

    *Take at least one step past the main task, in any direction, and use your agent as much as you like. It does not have to work. State what you tried, what you found, and where it is in this notebook.*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    First, we add costs for storing cartons, placing orders, and losing sales, then test reorder points from 10 to 80 to find which one has the lowest total cost. Next, we generate 365 days of random demand to see whether the recommended reorder point still works well over a full year instead of just 30 days. Then, we also change the number of cartons ordered each time to find the best combination of reorder point and order quantity. Finally, we add a slider and a chart so the owner can choose different reorder points and visually see how the inventory changes over the 30 days.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Add costs and test reorder points 10–80
    """)
    return


@app.cell
def _(simulate):
    def _():
        holding_cost = 0.50
        delivery_cost = 40
        lost_margin = 8
        print(f"{'Reorder':<10} {'Holding':<12} {'Delivery':<12} {'Lost Sales':<12} {'Total Cost':<12}")

        best_reorder_point = 0
        lowest_cost = float("inf")

        for reorder_point in range(10, 81):

            results = simulate(reorder_point)
            total_ending_stock = 0
            units_lost = 0
            orders_placed = 0
            for row in results:
                total_ending_stock += row["ending_stock"]
                units_lost += row["lost"]
                if row["units_ordered"] > 0:
                    orders_placed += 1
            # Calculate costs
            total_holding_cost = total_ending_stock * holding_cost
            total_delivery_cost = orders_placed * delivery_cost
            total_lost_cost = units_lost * lost_margin
            total_cost = (
                total_holding_cost
                + total_delivery_cost
                + total_lost_cost
            )
            print(
                f"{reorder_point:<10} "
                f"${total_holding_cost:<11.2f} "
                f"${total_delivery_cost:<11.2f} "
                f"${total_lost_cost:<11.2f} "
                f"${total_cost:<11.2f}"
            )
            # Find lowest cost
            if total_cost < lowest_cost:
                lowest_cost = total_cost
                best_reorder_point = reorder_point
        print()
        print(f"Best reorder point: {best_reorder_point}")
        return print(f"Lowest total cost: ${lowest_cost:.2f}")


    _()
    return


if __name__ == "__main__":
    app.run()
