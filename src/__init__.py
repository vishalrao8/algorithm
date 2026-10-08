from algorithm.sort.merge_sort import merge_sort_in_place

def main() -> None:
    arr = [1, 2, 10, 4, 9, 5, 9]
    merge_sort_in_place(arr)
    print(arr)

if __name__ == "__main__":
    main()
    