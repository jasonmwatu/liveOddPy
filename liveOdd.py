# Script to help guide place profitable bets from
# odds displayed during live betting
# liveOdd.py
# Jason Mwatu 2018-10-07
#

# Variables

# win_odd :         likely winner odds ** Wo
# draw_odd :        draw odds ** Do
# loss_odd :        loss odds ** Lo

# win_prob :        probability of win (reciprocal of win_odd) ** Wp
# draw_prob :       probability of draw (reciprocal of draw_odd) ** Dp
# loss_prob :       probability of loss (reciprocal of loss_odd)  ** Lp
# rest_prob :       1 - win_odd ** Rp
# good_prob :       acceptable sum of draw and loss probabilities for a profit ** Gp
# combined_prob :   sum of draw_prob and loss_prob ** Cp
# target_prob :     sum of win, draw and loss prob(also 1 - profit_margin),
#                   target_prob picked by me eg 0.9 or 90% for a profit margin of 10%

# profit_margin :   1 - target_prob ** T (Profit Threshold)

# win_stake :       amount to bet for a win - chosen pre-game; largest amount ** Sw
# draw_stake :      amount to bet for a draw = result_amount (divide) draw_odd ** Sd
# loss_stake :      amount to bet for a loss = result_amount (divide) loss_odd ** Sl
# total_stake :     total amount put into bet. Sum of win, draw and loss stake,
#                   total_stake = win_stake (divide) win_ratio (or stakes for draw or loss divided by their ratios)

# margin_amount :   the profit to be made after bet = profit_margin (multiply) total_stake
#                   or result_amount (divide) 1 + profit_margin
# result_amount :   total amount to be won by each bet,
#                   result_amount = win_stake (multiply) win_odd; also the sum of total_stake and margin_amount

# win_ratio :       win_prob (divide) target_prob
# draw_ratio :      raw_prob (divide) target_prob
# loss_ratio :      loss_prob (divide) target_prob

#############################################
#       Functions
#############################################


def setTarget(prob, thresh):
    rest_prob = 1 - prob
    out_prob = rest_prob - thresh
    return out_prob


def checkTarget():
    if combined_prob <= good_prob:
        return True
    else:
        return False


def getStake():
    draw_stake = result_amount / draw_odd
    loss_stake = result_amount / loss_odd
    all_stakes = [draw_stake, loss_stake]
    return all_stakes

#############################################
#       Getting values
#############################################

print('   Hello Gambler :)')
print('')
print('      Winning Odd: ')
win_odd = float(input())
print('      Winning Stake: ')
win_stake = float(input())
print('      Threshold/Profit margin:')
profit_margin = float(input())
print('')
print('  Getting Winning probability and prefered other probablities...')  # step 1

result_amount = win_odd * win_stake
win_prob = 1/win_odd  # step 2
good_prob = setTarget(win_prob, profit_margin)  # step 3 and 4

print('')
print('   Enter current Draw odds(live): ')
draw_odd = float(input())
print('   Enter current Loss odds(live): ')
loss_odd = float(input())  # Step 5

draw_prob = 1/draw_odd
loss_prob = 1/loss_odd  # step 6

combined_prob = draw_prob + loss_prob  # step 7

total_prob = win_prob + combined_prob
true_profit = 1 - total_prob

if checkTarget():
    stakes = getStake()
    total_stake = win_stake + stakes[0] + stakes[1]
    # total_stake2 = result_amount / (1 + true_profit)
    margin_amount = result_amount - total_stake
    print('')
    print('************************************')
    print('')
    print('   Place bets on the odds given:')
    print('      Draw: Odds = ' + str(draw_odd) + ' Stake = ' + str(stakes[0]))
    print('      Loss: Odds = ' + str(loss_odd) + ' Stake = ' + str(stakes[1]))
    print('')
    print('      Total amount to be won:   ' + str(result_amount))
    print('      Total amount bet:         ' + str(total_stake))
    print('      Profit:                   ' + str(margin_amount))
    print('')
    print('************************************')
else:
    print('')
    print('#####################################')
    print('')
    print('   Wait for odds to change or change the threshold(Profit margin)')
    print('')
    print('#####################################')
