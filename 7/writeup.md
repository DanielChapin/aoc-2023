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

# Part 2

For the second part, we can very easily modify our existing code to make `J` the lowest value card.
Now we just need to create an algorithm that determines what the best possible hand is.

There's a couple different ways that we can do this, but I think the most logical place to start is how we can use the jokers.

Let's say that we have $j$ jokers.
We want to figure out how we can use those jokers to modify the card counts to get the maximum rank hand type.
With each joker, we have a couple options:
1. Add a new card count (starting at 1)
2. Add to an existing card count
3. Leave it as a joker

Given that we have these three options, it's pretty obvious that we could just do a brute force search over the permutations (graph search); however, there's a really simple pattern we can use to simplify this.
Notice that adding to the highest existing card count always increases the value more than adding to any other card count, or leaving the card as a joker, unless the highest count is that of the jokers (in which case we can just leave them be).

```py
func hand_type(hand: Str) -> HandType:
    count_lookup: Dict<Card, Int> = counts of hand

    # `argmax` determines the key with the highest value.
    max_card = argmax(count_lookup)

    if Card.Joker not in count_lookup or max_card == Card.Joker:
        return HandType.from_card_counts(count_lookup)

    count_lookup[max_card] += count_lookup[Card.Joker]
    count_lookup.remove(Card.Joker)
    return Hand.from_card_counts(count_lookup)
```

## Correction

If the max card is the joker itself and we have another card, we just add all the jokers to that card.

```py
func hand_type(hand: Str) -> HandType:
    count_lookup: Dict<Card, Int> = counts of hand

    if Card.Joker not in count_lookup or len(count_lookup) == 1:
        return HandType.from_card_counts(count_lookup)

    # `argmax` determines the key with the highest value.
    max_card = argmax(count_lookup where key != Card.Joker)

    count_lookup[max_card] += count_lookup[Card.Joker]
    count_lookup.remove(Card.Joker)
    return Hand.from_card_counts(count_lookup)
```
