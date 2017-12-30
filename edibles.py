import numpy as np
import matplotlib.pyplot as plt


# Summary
#   So you're going to Edibles on University Avenue in the Neighborhood of the
#   Arts. It's a casual dining spot with eclectic eats and a location with a
#   history. The restaurant features tall tin ceilings, original hardwoods, and
#   a unique location in the Flatiron building, built in 1850. The food pulls
#   influences from Eastern Europe but blends it with typical New American fare.
#   Complemented by delicious cocktails and a spread of appetizers, you're sure
#   to have a great time!
#
#   This script is a Monte-Carlo simulation to determine the probability
#   distribution function for the price of a meal at Edibles, but tailored to
#   your specific preferences and to Edibles selection of menu items. I've used
#   this code to set the gift amount. The gift card amount is set based on the
#   50% confidence interval and the additional cash is set based on the 90%
#   one-sided confidence interval. Meaning, if you go out to eat at Edibles
#   every day of the year for the next 273 years (100,000 times), this gift card
#   and cash would cover the meal, tip, and tax 90% of the time.
#
#   The script pulls in menu pricing information and will stochastically and
#   iteratively formulate a meal. For example, one meal may have two appetizers
#   and the most expensive dessert whereas the next may only have one appetizer
#   and no dessert. All of these decisions are dictated by independent event
#   probability distribution functions. These are all then aggregated into an
#   overall meal price probability distribution function, from which the final
#   gift price is set.

# Input Description
#   For a given course, you have the option of getting 0, 1, or 2 items. The
#   probability of each event is specified in a numpy array. For example, if
#   there is a 50% chance two people will opt out of getting dessert, a 30%
#   chance they will share, and a 10% chance that both will get a dessert, then
#   the relative probabilities would be expressed as np.array([0.5, 0.3, 0.1])
#
# Assumptions:
#   - The $2 bacon add-on is not included for the 704 burger.
#   - The $26 appetizer sharing platter is excluded from the analysis.
#   - No wines are included in the analysis.
#   - I'm assuming you'll be going for dinner. No lunch menu items included
#   - I can't find the spiked coffee prices. Doesn't mean you shouldn't get one
#   - The $3 and $5 ice cream scoop add-on is excluded from the desserts.
#   - I'm going to lump salads in as a side option.
#   - There is no cross-correlation between the independent probabilities.


# If you get a drink. What are the chances it's going to be a cocktail?
prob_derek_gets_cocktail_over_beer = 0.7
prob_lauren_gets_cocktail_over_beer = 1.0

# What are the odds you would get a drink? 2 drinks?
prob_derek_gets_drink = np.array([0.0, 0.8, 0.2], dtype=float)
prob_lauren_gets_drink = np.array([0.2, 0.8, 0.0], dtype=float)

# Who wants an appetizer? I hear their pierogi's and borscht are pretty good.
prob_appetizer = np.asarray([0.2, 0.5, 0.3], dtype=float)

# The meal comes with a side, but if you're craving an extra serving of those
# truffle tots, throw on a side a la carte. Don't worry, they're low in carbs.
prob_side = np.asarray([0.5, 0.3, 0.2], dtype=float)

# Let's be real, you're both getting an entree. Lauren, probably the beef
# short rib. Derek, maybe the steak and frittes?
prob_entree = np.asarray([0.0, 0.0, 1.0], dtype=float)

# You're both getting a dessert. The question is, which one?
prob_dessert = np.asarray([0.2, 0.3, 0.5], dtype=float)

# How much do you think you're going to tip, remember this is pre tax. The
# breakdown is for 15%, 18%, and 20% respectively
prob_tip = np.asarray([0.1, 0.3, 0.6], dtype=float)
tax_options = np.asarray([0.15, 0.18, 0.20], dtype=float)

# What's the tax rate near you guys?
tax_rate = 0.08

# How many meals do you want to simulate?
n_runs = 100000

# So how much do all of these things cost?
cocktail_options = [8, 8, 9, 9, 9, 10, 10, 10, 12, 12]
beer_options = [6, 6, 6, 6, 6, 5, 6, 6]
appetizer_options = [15, 9, 14, 13, 14, 8, 14, 8, 16]
entree_options = [16, 20, 24, 30, 16, 26, 19, 27, 14, 27, 20]
side_options = [10, 9, 9, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5]
dessert_options = [7, 8, 7]

# Initalize the accumulated lists for the for loop
total = np.asarray([], dtype=float)
np.random.seed(42)

# We're going to simulate n number of meals to get a feel for how much things cost
for ind in  range(0, n_runs):

    # We need to initialize the cost of the individual courses for each meal
    cost_drinks = 0
    cost_appetizers = 0
    cost_entrees = 0
    cost_sides = 0
    cost_dessert = 0

    # Alright, how many drinks are Derek and Lauren going to get?
    derek_num_drinks = np.random.choice(range(0, len(prob_derek_gets_drink)), p=prob_derek_gets_drink)
    lauren_num_drinks = np.random.choice(range(0, len(prob_lauren_gets_drink)), p=prob_lauren_gets_drink)

    # Let's price out Derek's drinks
    for drink in range(0, derek_num_drinks):
        if np.random.rand() < prob_lauren_gets_cocktail_over_beer:
            cost_drinks += np.random.choice(cocktail_options)
        else:
            cost_drinks += np.random.choice(beer_options)

    # Let's price out Lauren's drinks
    for drink in range(0, lauren_num_drinks):

        # Here, we're checking if Lauren got a cocktail
        if np.random.rand() < prob_lauren_gets_cocktail_over_beer:
            cost_drinks += np.random.choice(cocktail_options)
        else:
            cost_drinks += np.random.choice(beer_options)

    # You're polish. Get the pierogi's or the borscht.
    num_appetizers = np.random.choice(range(0, len(prob_appetizer)), p=prob_appetizer)
    temp = [np.random.choice(appetizer_options) for ind in range(0, num_appetizers)]
    cost_appetizers += np.sum(temp)

    # Time to choose an entree, but do you really have a choice? (get the ribs)
    num_entrees = np.random.choice(range(0, len(prob_entree)), p=prob_entree)
    cost_entrees += np.sum([np.random.choice(entree_options) for ind in range(0, num_entrees)])

    # You need a side to help round out the meal
    num_sides = np.random.choice(range(0, len(prob_side)), p=prob_side)
    cost_sides += np.sum([np.random.choice(side_options) for ind in range(0, num_sides)])

    # I'm assuming dessert comes last, but who knows; I won't judge.
    num_desserts = np.random.choice(range(0, len(prob_dessert)), p=prob_dessert)
    cost_dessert += np.sum([np.random.choice(dessert_options) for ind in range(0, num_desserts)])

    # Okay, you're done eating. How about the tip and tax?
    pre_tax_total = cost_drinks + cost_appetizers + cost_entrees + cost_sides + cost_dessert
    tip = pre_tax_total*np.random.choice(tax_options, p=prob_tip)
    tax = pre_tax_total*tax_rate
    total = np.append(total, pre_tax_total + tip + tax)

# Calculate the gift card and cash value based on all of the meal possibilities
gift_card_value = np.percentile(total, 50)
cash_value = np.percentile(total, 90) - gift_card_value

# Print out the results to the command line
print 'Total Value: ${:3.2f}'.format(gift_card_value+cash_value)
print '  Gift Card: ${:3.2f}'.format(gift_card_value)
print '  Cash Value: ${:3.2f}'.format(cash_value)

# Visualize the cumulative distribution function
plt.plot(np.sort(total), np.linspace(0, 1, len(total)))
plt.xlim((60, 160))
plt.ylim((0, 1))
plt.xlabel('Meal Price [$]')
plt.ylabel('Cumulative Probability')
plt.show()

# Going to plot the probability distribution function as well for funsies
bins = np.arange(0, 1000, 2)
plt.plot([gift_card_value, gift_card_value], [0, 0.2], 'k--')
plt.plot([gift_card_value + cash_value, gift_card_value + cash_value], [0, 0.2], 'k')
plt.hist(total, bins, normed=1, facecolor='blue', alpha=0.5)
plt.xlim((60, 160))
plt.ylim([0, 0.025])
plt.xlabel('Meal Price [$]')
plt.ylabel('Probability')
plt.show()
