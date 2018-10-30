class lcsMap:
    lcsobjects = []
    lineId = 0

    def __init__(self):
        self.lcsobjects = []

    def insert(self, entry):
        list = entry.trim().split("[\\s]+")
        obj = getMatch(list)

    def getMatch(self, seq):
        bestMatchLength = 0
        for obj in self.lcsobjects:
            if (obj.length() < seq.length/2) || obj.length > seq.length * 2):
                continue;
            l = obj.getLCS(seq)
            if (l >= seq.length/2 && l > bestMatchLength):
                bestMatchLength = l
                bestMatch = obj

        return bestMatchLength

    def objectAt(self, index):
        return self.lcsobjects[i]

    def size(self):
        return len(self.lcsobjects)

    def toString(self):
        temp = "\t" + self.size() + "  Objects in the LCSMap\n\n"
        entryCount = 0

        for i in range(0, self.size()):
            temp = temp + "\tObject " + i + ":\n\t\t" + self.objectAt(i).toString() + "\n";
            entryCount += self.objectAt(i).count()

        temp = temp + "\n\t" + entryCount + " total entries found, " + self.lineId + " expected.";
        return temp


