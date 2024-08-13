#include <stdio.h>

int length(int Arr[], int size) {
    return size;
}

int bnrsch(int Arr[], int size, int Item) {
    int High = size - 1;
    int Low = 0;

    while (Low <= High) {
        int mid = (Low + High) / 2;
        if (Arr[mid] == Item) {
            return mid; 
        }
        else if (Arr[mid] > Item) {
            High = mid - 1;
        }
        else {
            Low = mid + 1;
        }
    }
    return -1;

int main(void) {
    int Arr[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = sizeof(Arr) / sizeof(Arr[0]);
    int Item = 7;
    int result = bnrsch(Arr, size, Item);
    
    if (result != -1) {
        printf("Item found at index %i\n", result);
    } else {
        printf("Item not found\n");
    }

    return 0;
}