class Solution:
    def __init__(self):
        self.sell_map = dict()

    def shoppingOffers(self, price: 'List[int]', special: 'List[List[int]]', needs: 'List[int]') -> 'int':
        # Evaluate the cost without applying any special offer
        cost = sum(needs[i] * price[i] for i in range(len(needs)))
        # For each special offer, check if the offer is appliable
        for offer in special:
            current_needs = [needs[i] - offer[i] for i in range(len(needs))]
            # If the offer is appliable, find its minimum cost for fullfilling current_needs
            if min(current_needs) >= 0:
                cost = min(cost, self.sell_map.get(tuple(current_needs), self.shoppingOffers(price, special, current_needs) + offer[-1]))
        # Memoize the cost for current needs
        self.sell_map[tuple(current_needs)] = cost
        return cost
special = [[3,0,5],[1,2,10]]
needs = [3,2]
print(Solution().shoppingOffers(prices, special, needs))