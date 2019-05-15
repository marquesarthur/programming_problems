def cellCompete(states, days):
    # WRITE YOUR CODE HERE

    if days <= 0:
        return states

    current = [0 for _ in states]
    for d in xrange(0, days):
        for i in xrange(len(states)):
            prev_house = states[i - 1] if i > 0 else 0
            next_house = states[i + 1] if i < len(states) - 1 else 0
            current[i] = prev_house ^ next_house

        states = [h for h in current]

    return states


print(cellCompete([1, 0, 0, 0, 0, 1, 0, 0], 1))