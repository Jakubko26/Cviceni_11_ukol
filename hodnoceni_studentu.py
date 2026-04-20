class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        body = self.scores[index]

        if body >= 90:
            return "A"
        if body >= 80:
            return "B"
        if body >= 70:
            return "C"
        if body >= 60:
            return "D"
        if body >= 50:
            return "E"
        else:
            return "F"
    def find(self,pocet_bodu):
        result = []
        for i, body in enumerate(self.scores):
            if body == pocet_bodu:
                result.append(i)
        return result
    def get_sorted(self):
        scores = list(self.scores)

        dlzka = len(scores)

        for i in range(dlzka):
            for j in range(0, dlzka -i -1):
                if scores[j] > scores[j+1]:
                    scores[j], scores[j +1] = scores[j+1], scores[j]
        return scores

def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print("Pocet studentov", results.count())
    for i in range (results.count()):
        print(f"Student {i}: {results.get_by_index(i)} body: {results.get_grade(i)}")
    print("Indexy pre 100:",results.find(100) )
    print("Serazene vysledky:",results.get_sorted() )
    from sorting import random_numbers

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())
if __name__ == "__main__":
    main()