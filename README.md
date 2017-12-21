# Restaurant Pricing
Don't know how much a meal is going to cost? It's obvious, run a Monte-Carlo simulation.

So you're going to [Edibles](http://ediblesrochester.com) on University Avenue in the Neighborhood of the Arts. It's a casual dining spot with eclectic eats and a location with a history. The restaurant features tall tin-roof ceilings, original hardwoods, and a unique location in the flat-iron building.

![alt text](https://s3-media1.fl.yelpcdn.com/bphoto/6bk_Qe5vbkCl5VVjqcxHFA/o.jpg)

## Code Description
The following code is a Monte-Carlo simulation to determine the probability distribution function for the price of a meal at Edibles, but tailored to your specific preferences and to Edibles selection of menu items. I've used this code to set the gift amount. The gift card amount is set based on the 50% confidence interval and the additional cash is set based on the 90% confidence interval. Meaning, if you go out to eat at Edibles every day of the year for the next 273 years (100,000 times), this gift card and cash would cover the whole meal, tip, and tax 90% of the time.

## Results
I know, this is terrible practice. But for the purposes of this gift, I'm going to assume the results are static and summarize in the markdown file. Let's get started.

The meal price probability distribution function for (my interpretation of) your preferences is shown below. The price specified by the 50th percentile is given in the form of a gift card. To ensure you don't get stuck with unused gift card monies, the remaining balance to get you up to the 90th percentile will be given in the form of cash.

![alt text](./img/pdf_edibles_100000.png)

To summarize, here is the total value of the gift.

Total Value: $141.44
  Gift Card: $115.62
  Cash Value: $25.82
