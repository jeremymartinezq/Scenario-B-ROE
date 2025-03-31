import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Define the annual growth rates and investments for Scenario B
years = np.array([1, 2, 3, 4, 5])
initial_investment = 1000000
additional_investment_per_year = 200000 * 5  # $200,000 per stock annually
annual_returns = np.array([1238800, 1295825.44, 1309443.12, 1312695.02, 1313471.57])  # Portfolio values

# Calculate the cumulative investments and returns
cumulative_investment = np.array([initial_investment] + [initial_investment + additional_investment_per_year * i for i in range(1, 5)])
cumulative_returns = np.cumsum(annual_returns)

# Initialize payback period
payback_period = None

# Find the payback period
for i in range(len(cumulative_returns)):
    if cumulative_returns[i] >= cumulative_investment[i]:
        payback_period = years[i]
        break

# Create a custom formatter function for dollars
def dollar_formatter(x, pos):
    return '${:,.0f}'.format(x)

# Plotting the data
fig, ax = plt.subplots(figsize=(14, 8))

# Plot cumulative investment
ax.plot(years, cumulative_investment, marker='o', linestyle='-', color='blue', label='Cumulative Investment ($)', linewidth=2)

# Plot cumulative returns
ax.plot(years, cumulative_returns, marker='o', linestyle='-', color='green', label='Cumulative Returns ($)', linewidth=2)

# Adding annotations for clarity
for i, (investment, returns) in enumerate(zip(cumulative_investment, cumulative_returns)):
    ax.text(years[i], investment + 50000, f"${investment:,.0f}", ha='center', fontsize=10, color='blue')
    ax.text(years[i], returns + 50000, f"${returns:,.0f}", ha='center', fontsize=10, color='green')

# Highlight the payback period
if payback_period:
    ax.axvline(x=payback_period, color='red', linestyle='--', label='Payback Period')
    ax.text(payback_period, max(cumulative_returns), f'Payback Period\nYear {payback_period}', color='red', va='bottom')

# Adding title and labels
plt.title("Payback Period Calculation for Portfolio (Scenario B)", fontsize=16)
plt.xlabel("Years", fontsize=14)
plt.ylabel("Dollars", fontsize=14)
plt.legend()
plt.grid(True)

# Format y-axis with dollar amounts
ax.yaxis.set_major_formatter(FuncFormatter(dollar_formatter))

# Show plot
plt.show()

# Print the payback period
if payback_period:
    print(f"Payback Period: Year {payback_period}")
else:
    print("The cumulative returns did not exceed the cumulative investment within the given years.")
