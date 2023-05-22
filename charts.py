import heap
import random
import time
import matplotlib.pyplot as plt
import gc


if __name__ == '__main__':

    testing_list = [random.randint(1, 300000) for _ in range(100000)]
    first_n_numbers = [i for i in range(10000, 100001, 10000)]
    times_heap_insert_2 = [] # tablica z czasami bst insert
    times_heap_insert_5 = []
    times_heap_insert_7 = []
    times_heap_max_extract_2 = []
    times_heap_max_extract_5 = []
    times_heap_max_extract_7 = []

    # # ----------------------------------------------------------------------
    # #  INSERT
    # # ----------------------------------------------------------------------

    # 2
    for n in first_n_numbers:

        gc_old = gc.isenabled()
        gc.disable()

        heap_insert_start = time.process_time()

        h = heap.MaxHeap(2)
        for i in range(n):
            h.insert(testing_list[i])

        heap_insert_stop = time.process_time()

        if gc_old:
            gc.enable()

        times_heap_insert_2.append(heap_insert_stop - heap_insert_start)

    # ----------------------------------------------------------------------
    # 5
    for n in first_n_numbers:

        gc_old = gc.isenabled()
        gc.disable()

        heap_insert_start = time.process_time()

        h = heap.MaxHeap(5)
        for i in range(n):
            h.insert(testing_list[i])

        heap_insert_stop = time.process_time()

        if gc_old:
            gc.enable()

        times_heap_insert_5.append(heap_insert_stop - heap_insert_start)

    # ----------------------------------------------------------------------
    # 7
    for n in first_n_numbers:

        gc_old = gc.isenabled()
        gc.disable()

        heap_insert_start = time.process_time()

        h = heap.MaxHeap(7)
        for i in range(n):
            h.insert(testing_list[i])

        heap_insert_stop = time.process_time()

        if gc_old:
            gc.enable()

        times_heap_insert_7.append(heap_insert_stop - heap_insert_start)

    # ----------------------------------------------------------------------

    plt.plot(times_heap_insert_2, label="2")
    plt.plot(times_heap_insert_5, label="5")
    plt.plot(times_heap_insert_7, label="7")
    plt.title('Czas wstawiania')
    plt.xlabel('Liczba elementów')
    plt.ylabel('Czas')
    plt.legend()
    plt.xticks(range(len(first_n_numbers)), first_n_numbers)
    plt.savefig('Czas_wstawiania.jpg', dpi=100)
    plt.show()

    # ----------------------------------------------------------------------
    #  EXTRACT_MAX
    # ----------------------------------------------------------------------

    # 2
    for n in first_n_numbers:
        h = heap.MaxHeap(2)
        for i in range(n):
            h.insert(testing_list[i])

        gc_old = gc.isenabled()
        gc.disable()

        heap_extract_max_start = time.process_time()
        for i in range(n):
            h.heap_extract_max()

        heap_extract_max_stop = time.process_time()

        if gc_old:
            gc.enable()

        times_heap_max_extract_2.append(heap_extract_max_stop - heap_extract_max_start)

    # ----------------------------------------------------------------------
    # 5
    for n in first_n_numbers:
        h = heap.MaxHeap(5)
        for i in range(n):
            h.insert(testing_list[i])

        gc_old = gc.isenabled()
        gc.disable()

        heap_extract_max_start = time.process_time()

        for i in range(n):
            h.heap_extract_max()

        heap_extract_max_stop = time.process_time()

        if gc_old:
            gc.enable()

        times_heap_max_extract_5.append(heap_extract_max_stop - heap_extract_max_start)

    # ----------------------------------------------------------------------
    # 7
    for n in first_n_numbers:
        h = heap.MaxHeap(7)
        for i in range(n):
            h.insert(testing_list[i])

        gc_old = gc.isenabled()
        gc.disable()

        heap_extract_max_start = time.process_time()

        for i in range(n):
            h.heap_extract_max()

        heap_extract_max_stop = time.process_time()

        if gc_old:
            gc.enable()

        times_heap_max_extract_7.append(heap_extract_max_stop - heap_extract_max_start)

    # ----------------------------------------------------------------------

    plt.plot(times_heap_max_extract_2, label="2")
    plt.plot(times_heap_max_extract_5, label="5")
    plt.plot(times_heap_max_extract_7, label="7")
    plt.title('Czas usuwania największej wartości')
    plt.xlabel('Liczba elementów')
    plt.ylabel('Czas')
    plt.legend()
    plt.xticks(range(len(first_n_numbers)), first_n_numbers)
    plt.savefig('Czas_usuwania_najwiekszej_wartosci.jpg', dpi=100)
    plt.show()