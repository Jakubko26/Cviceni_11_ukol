import random
import matplotlib.pyplot as plt

def bubble_sort(numbers):
    numbers = numbers[:]
    dlzka = len(numbers)
    plt.ion()
    plt.show()
    for i in range(dlzka):
        for j in range(0, dlzka -i -1):
            if numbers[j] > numbers[j +1]:
                numbers[j], numbers[j +1] = numbers[j+1], numbers[j]
        index_highlight1 = j
        index_highlight2 = j + 1
        colors = ["steelblue"] * len(numbers)
        colors[index_highlight1] = "tomato"
        colors[index_highlight2] = "tomato"
        plt.clf()
        plt.bar(range(len(numbers)), numbers, color=colors)
        plt.title("Bubble Sort")
        plt.pause(0.1)

    return numbers
plt.ioff()
plt.show()

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(numbers):
    numbers = numbers[:]

    for pozice_cisla in range(len(numbers)):
        min_indx = pozice_cisla
        for pozice_prochazeni in range(pozice_cisla +1, len(numbers)):
            if numbers[pozice_prochazeni] < numbers[min_indx]:
                min_indx = pozice_prochazeni

        numbers[pozice_cisla], numbers[min_indx] = numbers[min_indx], numbers[pozice_cisla]
    return numbers





numbers = [5, 1, 4, 2, 8]
print("Puvodni seznam:", numbers)
print("Novy seznam:", selection_sort(numbers))
print("Bubble sort:", bubble_sort(numbers))

rnd = random_numbers(20)
print("Náhodný:", rnd)
print("Novy seznam:", selection_sort(rnd))
print("Bubble sort:", bubble_sort(rnd))