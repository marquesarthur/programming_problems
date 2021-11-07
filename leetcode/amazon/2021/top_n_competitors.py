from collections import defaultdict


def topNumCompetitors(numCompetitors, topNCompetitors, competitors, numReviews, reviews):
    total = defaultdict(int)
    for competitor in competitors:
        total[competitor] = 0

    for review in reviews:
        prior = dict(total)

        for word in review.split():
            if word in total and prior[word] + 1 != total[word]:
                total[word] += 1

    result = sorted([(key, value) for key, value in total.items()],
                    key=lambda k: k[1], reverse=True)
    result = [key for key, value in result][:topNCompetitors]
    return result


numReviews = 6
numCompetitors = 6
topNCompetitors = 2
competitors = [
    "newshop", "shopnow", "afashion",
    "fashionbeats", "mymarket", "tcellular"
]
reviews = [
    "newshop is providing good services in the city; everyone should use newshop",
    "best services by newshop",
    "fashionbeats has great services in the city",
    "I am proud to have fashionbeats",
    "mymarket has awesome services",
    "Thanks Newshop for the quick delivery"
]

print(topNumCompetitors(numCompetitors, topNCompetitors,
                        competitors, numReviews, reviews))
