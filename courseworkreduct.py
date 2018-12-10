
"""
Ensure (a) is correct
>>> seriesScore(("bob", [2, 4, 1, 1, 2, 5]))
10
>>> seriesScore(("bill", [1, 3, 1, 4, 2, 4]))
11
Ensure (b) is correct
>>> ascSailors([  1, 1, 1]), ('Clare', [2, 3, 2, 2, 4, 2]), ('Bob', [3, 1, 5, 3, 2, 5]), ('Dennis', [5, 4, 4, 4, 3, 4]), ('Eva', [4, 5, 3, 5, 5, 3])]
Ensure (c) is correct
>>> ReadCSV("sailors.csv")
OrderedDict([('Alice', (100.0, 0.0)), ('Bob', (100.0, 5.0)), ('Clare', (100.0, 10.0)), ('Dennis', (90.0, 0.0)), ('Eva', (90.0, 5.0))])
Ensure (d) is correct
>>> rndPerformance(ReadCSV("sailors.csv"))
OrderedDict([('Alice', 100.0), ('Bob', 105.76045089520113), ('Clare', 108.36452152548142), ('Dennis', 90.0), ('Eva', 96.10844089749128)])
Ensure (e) is correct
>>> sailorPosition(rndPerformance(ReadCSV("sailors.csv")))
['Clare', 'Bob', 'Alice', 'Eva', 'Dennis']
"""
import collections
import random
import csv
# mport opperator

#(a)


def seriesScore(sailor):
    '''function to return sum of a sailors 
    scores with worsed score ommited.
    function takes a tuble of a salior's name and scores
    >>>seriesScore(("Sailor's name",[list scores]))'''

    scores = sailor[1]
    # takes the list of scores out the tuble
    scores = sorted(scores, reverse=False)
    # sorts in decending order
    scores.pop()
    # remove worst score
    return (sum(scores))


#(b)


def sortSeries(sailors):
    '''function to spor a complete series of races in decending order
    (winner first looser last).
    take a single list of tubles of sailors scores.
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

#(c)


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

#(d)


def generatePerformances(sailorPerformance):
    '''function to generate random performance value based on 
    mean performance and standerd deviation
    takes dictionary returned from readCSV
    >>>generatePerformances({sailor1:[meanPerfromance, stdDeviation],
    sailor2:[meanPerfromance, stdDeviation]},...)'''
    random.seed()

    # Define an ordered dictionary to input the data into
    PerformanceVal = {}
    for key in sailorPerformance:  # go through each key
        meandev = sailorPerformance[key]  # take out the tuple
        print(meandev)
        PerformanceVal[key] = random.normalvariate(meandev[0], meandev[1])

    return PerformanceVal

#(e)


def sailorPosition(PerformanceVal):
    '''sailors postions returns and odered list of keys
     from generatePerformances
     sailorPosition({"salior1":[performanceVal], "salior2":performanceVal},...)'''
    Positions = sorted(
        PerformanceVal, key=lambda val: PerformanceVal[val], reverse=False)
    return Positions

#(f)


def calculateFinishingOrder(results):
    '''Run race takes a tuple of saliors name
    and an empty list each call adds a race
    result to the list
    >>>runRace(("sailor'sname",[]))'''
    used = []

    for key in results:
        rndNum = random.randrange(1, 6, 1)
        while rndNum in used:
            rndNum = random.randrange(1, 6, 1)

        results[key].append(rndNum)
        used.append(rndNum)
    return results


def main():
    results = dict([('Alice', []), ('Bob', []), ('Clare', []),
                    ('Dennis', []), ('Eva', [])])

    # runs 5 races
    for races in range(0, 6):
        results = calculateFinishingOrder(results)
    #prints results of races 
    print(results)

    for key in results:
        results[key] = seriesScore((key, results[key]))

    print(results)
    results = sailorPosition(results)

    print(results)


main()
