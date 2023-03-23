"""
Shareforce Testing environment

Algorithmic Trading

Example:
Let’s use sol-za as an example with the data below:
Date        Price
29-Dec-06   258.79
02-Jan-07   259.50
03-Jan-07   249.35
04-Jan-07   241.40
05-Jan-07   239.00
08-Jan-07   238.90
09-Jan-07   233.95
10-Jan-07   230.97
• On 3 Jan 2007, the price dropped 3.91% (259.50 to 249.35), so that's our entry to buy at \
249.35 since it dropped by more than 3%
• 5 trading days later, on 10 Jan 2007, we sell at 230.97.
• In this trade we made a loss of 7.37% which leaves us with 92.63% of our starting cash balance
Assume in the next trade we made a gain of 15%:
• Our return for this strategy is now 6.52% and we have 106.52% of our starting cash balance.
• Note that the gains and losses build on each other

"""
import sys

# Trading Program Constant Values
SHARE_BUY_PERCENT = 3.0
DAYS_TO_HOLD = 10
FILE_NAME = "data.csv"
CHECK_COMPANIES = [
    # 'omn-za',
    # 'rem-za',
    'sol-za',
    # 'afe-za',
    # 'kap-za',
    # 'mrp-za',
    # 'whl-za'
]

def algo_trading():
    """Algorithm Trading Forecasting."""
    transactions_map = {}   # Dict to store companies and asscociated dates and prices
    transaction_result_dict = {}   # Dict to store companies and asscociated results
    transaction_percent_dict = {}  # Dict to store companies and asscociated returns

    # Open File to read transactions
    file_name = FILE_NAME
    with open(file_name) as f:
        transactions = f.read()

    transactions = transactions.rstrip('\n')  # Removing trailing newline
    transaction_data = transactions.split('\n')  # Split data on newlines
    del transaction_data[0]  # Remove Header

    # Store transactions in a mapped dictionary per company
    for t in transaction_data:
        trade = t.split(',')  # Split transaction line per comma into date and price
        # Add company if not a key in transactions_map already
        if trade[0] not in transactions_map:
            transactions_map[trade[0]] = []
        # Add company if not a key in transaction_result_dict already
        if trade[0] not in transaction_result_dict:
            transaction_result_dict[trade[0]] = {}
        # Add company if not a key in transaction_result_dict already
        if trade[0] not in transaction_percent_dict:
            transaction_percent_dict[trade[0]] = {}
        # Add date and price transaction to company dict
        transactions_map[trade[0]].append([trade[1], trade[2]])

    total_return = 0.0
    percent_loss_gain = 0.0
    combined_total = 0.0
    cash_balance_percentage = 100.0
    prev_percent_update = 0.0

    # Remove Companied you're not checking
    for key in list(transactions_map):
        if key not in CHECK_COMPANIES:
            del transactions_map[key]
            del transaction_result_dict[key]
            del transaction_percent_dict[key]

    # Calculate Returns
    for company in transactions_map:
        no_transactions = len(transactions_map[company])
        # Set latest price to first price in the list
        latest_price = float(transactions_map[company][0][1])
        for x, item in enumerate(transactions_map[company][1:], start=1):
            previous_price = latest_price
            latest_price = float(item[1])
            percent_diff = ((previous_price - latest_price) / previous_price) * 100

            # Buy if percentage diff is above SHARE_BUY_PERCENT threshold set
            if percent_diff > SHARE_BUY_PERCENT:
                bought_price = latest_price
                total_return += bought_price

                trading_days_index = x + DAYS_TO_HOLD
                # Check if we've gone past the available data_set or not
                if trading_days_index >= no_transactions:
                    break
                sold_price_diff = float(transactions_map[company][x + DAYS_TO_HOLD][1]) - latest_price
                percent_update = (sold_price_diff / latest_price) * 100
                # current_percent_update = prev_percent_update + percent_update
                # prev_percent_update = percent_update
                # Todo: Confirm compounding gains and losses return calculation
                cash_balance_percentage += percent_update
                total_return += sold_price_diff

        transaction_result_dict[company] = total_return
        transaction_percent_dict[company] = cash_balance_percentage
        combined_total += total_return

    # Calculate min, max and average returns across companies
    min_return = round(min(transaction_result_dict.values()), 2)
    max_return = round(max(transaction_result_dict.values()), 2)
    average_return = round(combined_total / float(len(transaction_result_dict)), 2)
    for i, x in transaction_result_dict.items():
        transaction_result_dict[i] = round(x, 2)
    for i, x in transaction_percent_dict.items():
        transaction_percent_dict[i] = round(x, 2)

    print("~o~o~o~o~o~o TRADING RESULTS o~o~o~o~o~o~")
    print("-----------------------------------------")
    print(f"Min Return: {min_return}")
    print(f"Max Return: {max_return}")
    print(f"Average Return: {average_return}")
    print(f"Transaction Results: {transaction_result_dict}")
    print(f"Transaction Return Percentages: {transaction_percent_dict}")
    print("-----------------------------------------")
    return


if __name__ == '__main__':
    input = ' '.join(sys.argv[1:])

    algo_trading()


"""
Question Answers:
=================

Question 1
For SOL-za, what is the return over the period?
Return is 87261.70 or an increase of 459.55%

Question 2
What is the min, max and average return for all the companies over the period?
Min Return: 11644.68
Max Return: 165144.93
Average Return: 104454.48

Question 3
If the decide to only by buy the share dropped by 4% or more, what is the return in this
case for each company?
'omn-za': 5792.51, 18.3%,
'rem-za': 11685.68, 32.88%
'sol-za': 54711.09, 178.26%
'afe-za': 58863.84, 184.07%
'kap-za': 59487.54, 453.46%
'mrp-za': 72836.74, 486.1%
'whl-za': 75795.4, 562.91%

Question 4
If the decide to hold for 10 days, what is the return in this case for each company?
(with a 3% drop)
'omn-za': 11521.38, -141.65%
'rem-za': 29432.93, -10.86%
'sol-za': 116614.88, 622.19%
'afe-za': 125575.0, 684.59%
'kap-za': 126697.27, 1209.79%
'mrp-za': 155330.55, 1615.29%
'whl-za': 165215.21 1943.18%

Question 5
From the results above, do you expect this strategy to be successful going forward?
For the most part, according to my results, yes I do
"""
