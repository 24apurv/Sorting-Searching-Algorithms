# Time Complexity - O(n^2)

def main():

    # array takes in space separated numbers from the user
    array = list(
        map(int, input("Enter the numbers separated with space: ").strip().split(" ")))

    # Calling the binary search method
    output = bubble_sort(array)
    print(f"The sorted array is: {output}")

    


# Recursive implementation of binary search
def bubble_sort(array):

    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[i] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    
    return array

if __name__ == "__main__":
    main()
