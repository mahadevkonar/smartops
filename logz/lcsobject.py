class lcsObject:
    lineIds = []
    lcsSeq = []

    def __init__(self, lcsSeq, lineIds):
        self.lineIds.append(lineIds)
        self.lcsSeq = lcsSeq

    def getLCS(self, seq):
        count = 0
        lastMatch = -1
        for i in range(0, len(self.lcsSeq)):
            if (self.lcsSeq[i] == "*"):
                continue

            for j in range(lastMatch + 1, len(seq)):
                if (self.lcsSeq[i] == seq[j]):
                    lastMatch = j
                    count++
                    break

        return count

    def insert(self, seq, lineId):
        self.lineIds.append(lineId)
        temp = ""
        lastMatch = -1
        placeholder = False
        for k in range(0, len(self.lcsSeq)):
            if (self.lcsSeq[i] == "*"):
                if not placeholder:
                    temp = temp + "*"
                placeholder = True
                continue
            for j in range(lastMatch + 1, len(seq)):
                if (self.lcsSeq[i] == seq[j]):
                    placeholder = False
                    temp = temp + self.lcsSeq[i] + " "
                    lastMatch = j
                    break
                elif (not placeholder):
                    temp = temp + "*"
                    placeholder = True
        self.lcsSeq = temp.strip().split("[\\s]+")

    def length(self):
        return len(self.lcsSeq)

    def count(self):
        return len(self.lineIds)

    def toString(self):
        temp = ""
        for s in self.lcsSeq:
            temp = temp + s + " "
        temp = temp + "\n\t\t{"
        for i in self.lineIds:
            temp = temp + i + ", "
        return temp[0:len(temp)-2] + "}"



