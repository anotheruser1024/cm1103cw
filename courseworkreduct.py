import random
import csv
from operator import itemgetter
numberOfraces = 6

'''(a)'''


def seriesScore(sailor, removeScores=1):
    '''function to return sum of a sailors
    scores with worsed score ommited.
    function takes a tuple of a salior's name and scores
    >>>seriesScore(("Sailor's name",[list scores]), remove sores)'''

    scores = sailor[1]
    # takes the list of scores out the tuple
    scores = sorted(scores, reverse=False)
    # sorts in decending order
    if removeScores == 1:
        scores.pop()
        del scores[0]
    # remove worst score
        return (sum(scores))
    else:
        removeScores = len(scores) - removeScores
        return(sum(scores[0:removeScores]))


'''(b)'''


def sortSeries(sailors):
    '''function to spor a complete series of races in decending order
    (winner first looser last).
    take a single list of tuples of sailors scores.
    [("sailor1",[list of scores]), ("sailor2",[listofScores])]
    >>>sortSeries([list of all saliors])'''

    if len(sailors) > 1:
        pivot = round(len(sailors) / 2)
        bigger = []
        smaller = []

        for i, sailor in enumerate(sailors):
            if i != pivot:
                if seriesScore(sailor) > seriesScore(sailors[pivot]):
                    bigger.append(sailor)
                else:
                    smaller.append(sailor)

        # Recursion to continue comparsions until both lists are sorted
        sortSeries(smaller)
        sortSeries(bigger)

        # once recursion is complete, return the sorted list
        return (smaller + [sailors[pivot]] + bigger)


'''(c)'''


def readCsv(filename):
    '''ReadCSV takes a file path as a string "/filepath/fileName.csv"
        and returns an odered Dictionary of saliors
        name:(performace and standerd deviation)
        >>>readCsv("/filepath/fileName.csv")'''
    path = filename
    file = open(path, newline="")
    reader = csv.reader(file)
    header = next(reader)  # first line is assummed to be header

    sailorsPerformance = {}
    for row in reader:
        # row name, mean performance, std dev (standerd deviation)
        name = row[0]
        meanPerformance = float(row[1])
        stdDev = float(row[2])
        sailorsPerformance[name] = (meanPerformance, stdDev)

    return sailorsPerformance


'''(d)'''


def generatePerformances(sailorPerformance):
    '''function to generate random performance value
    based on mean performance and standerd deviation
    takes dictionary returned from readCSV
    >>>generatePerformances({sailor1:[meanPerfromance, stdDeviation],
    sailor2:[meanPerfromance, stdDeviation]},...)'''
    # random.seed()

    # Define an ordered dictionary to input the data into
    PerformanceVal = {}
    for key in sailorPerformance:  # go through each key
        meandev = sailorPerformance[key]  # take out the tuple
        PerformanceVal[key] = random.normalvariate(meandev[0], meandev[1])

    return PerformanceVal


'''(e)'''


def calculateFinishingOrder(PerformanceVal):
    '''sailors postions returns and odered list of keys
     from generatePerformances
     >>>sailorPosition({"salior1":[performanceVal],
     "salior2":performanceVal})'''
    Positions = sorted(
        PerformanceVal, key=lambda val: PerformanceVal[val], reverse=True)
    return Positions


'''(f)'''


def main():

    sailors = readCsv("results.csv")
    results = {}
    for name in sailors:
        results[name] = []

    print(results)

    for i in range(numberOfraces):
        simulation = generatePerformances(sailors)
        pos = calculateFinishingOrder(simulation)

        for score, name in enumerate(pos, start=1):
            results[name].append(score)

    print()
    print(results)
    print("")
    series = sortSeries(list(results.items()))
    for i in series:
        print(series.index(i) + 1, i[0], i[1])

    scores = []

    for sailorsscore in (list(results.items())):
        scores.append(list((sailorsscore[0], seriesScore(sailorsscore))))

    scores = sorted(scores, key=itemgetter(1))
    print("\t" + ("_" * (len("Series Ranking by score") + 4)))
    print()
    print("\t~ Series Ranking by score ~")
    print("\t" + ("_" * (len("Series Ranking by score") + 4)))
    print()
    for i in scores:
        print("\t{:>2}{:>10}{:>10}".format(scores.index(i) + 1, i[0], i[1]))


if __name__ == '__main__': main()


