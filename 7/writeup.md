# Day 7

So I think the most logical first step for this problem is just parsing the hands.
Given that there's no flushes or anything like that where the order of the cards matters for identifying the hand, I think the best first step would be to just count up all the cards and then just look at the counts.
Five of a kind: $(5, x)$
Four of a kind: $(4, x), (1, y)$
Three of a kind: $(3, x), (1, y), (1, z)$
Two pair: $(2, x), (2, y), (1, z)$
One pair: $(2, x), (1, y), (1, z), (1, w)$
High card: $(1, v), (1, w), (1, x), (1, y), (1, z)$
Note that if we sort these by the quantity then we can easily identify what kind of hand it is in $O(n)$.
Also note that the type of cards doesn't matter here, only the quantities, meaning that we can just do a lookup on the numbers using multisets (or sorted lists) so we can ignore order!

To finalize the identification of the hand, we just need to know the first card in the hand, and the bid on the hand.
$\text{identity}(h) = (\text{type}(h), \text{card}_0(h), \text{bid}(h))$.
Now to sort hands, we sort by first the type and second by the first card.
