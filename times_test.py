import time
import matplotlib.pyplot as plt
from search import nfind, kmpfind, karp_rabin_search, Rabin_Karp_Matcher, KR_find

with open("pan-tadeusz.txt", "r", encoding="utf-8") as file:
    full_text = file.read()


def get_first_n_words(text, n):
    """
    Extracts the first n words from the given text.

    Args:
        text (str): The text to extract words from.
        n (int): The number of words to extract.

    Returns:
        str: A string containing the first n words of the text.
        str: A string containing the whole text but just words.
    """
    words = text.split()  # Split the text into words
    return (' '.join(words[:n]), ' '.join(words))  # Join the first n words and also return text


def measure_time(search_function, pattern, text, n):
    """
    Measure the average time taken by a search function to find a pattern in a text.

    Args:
        search_function (function): The search function to be measured.
        pattern (str): The pattern to search for.
        text (str): The text to search in.
        n (int): The number of times to run the search function.

    Returns:
        float: The average time taken by the search function, in seconds.
    """
    start_time = time.time()
    for _ in range(n):
        search_function(pattern, text)
    end_time = time.time()
    return (end_time - start_time)/n


def generate_plots(text, n_values):
    """
    Generates plots comparing the execution times of different pattern matching algorithms.

    Args:
        text (str): The text to search in.
        n_values (list): A list of integers representing the lengths of subtexts to consider.

    Returns:
        None
    """
    naive_times = []
    kmp_times = []
    karp_rabin_times = []
    karp_rabin_times2 = []
    karp_rabin_times3 = []
    for n in n_values:
        # Przygotowanie podciągu tekstu o długości n
        sub_text, text = get_first_n_words(text, n)
        print("Debug")

        # Pomiar czasu dla algorytmu naiwnego
        naive_time = measure_time(nfind, sub_text, text, 10)
        naive_times.append(naive_time)

        # Pomiar czasu dla algorytmu KMP
        kmp_time = measure_time(kmpfind, sub_text, text, 10)
        kmp_times.append(kmp_time)

        # Pomiar czasu dla algorytmu Karpa-Rabina
        karp_rabin_time = measure_time(karp_rabin_search, sub_text, text, 10)
        karp_rabin_times.append(karp_rabin_time)

        karp_rabin_time2 = measure_time(Rabin_Karp_Matcher, sub_text, text, 10)
        karp_rabin_times2.append(karp_rabin_time2)

        karp_rabin_time3 = measure_time(KR_find, sub_text, text, 10)
        karp_rabin_times3.append(karp_rabin_time3)


    # Generowanie wykresu
    plt.plot(n_values, naive_times, label='Naiwny')
    plt.plot(n_values, kmp_times, label='KMP')
    plt.plot(n_values, karp_rabin_times, label='Karp-Rabin')
    plt.plot(n_values, karp_rabin_times2, label='Karp-Rabin-2')
    plt.plot(n_values, karp_rabin_times3, label='Karp-Rabin-3')
    plt.xlabel('Liczba szukanych słów')
    plt.ylabel('Czas wykonania (s)')
    plt.title('Porównanie algorytmów wyszukiwania wzorca')
    plt.legend()
    plt.show()


# Przeprowadzenie testów dla n od 100 do 1000 z krokiem 100
n_values = list(range(100, 1100, 100))
generate_plots(full_text, n_values)
