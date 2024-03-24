#include <iostream>
using namespace std;

void insertionSort(int arr[], int length)
{
  int i, key, j;
  for (i = 1; i < length; i++)
  {
    key = arr[i];
    j = i - 1;

    while (j >= 0 && arr[j] > key)
    {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = key;
  }
}

void printArray(int arr[], int length)
{
  for (int i = 0; i < length; i++)
  {
    cout << arr[i] << " ";
  }
  cout << endl;
}

int main()
{
  int arr[] = {12, 11, 13, 5, 6};
  int length = sizeof(arr) / sizeof(arr[0]);

  cout << "Original array: ";
  printArray(arr, length);

  insertionSort(arr, length);

  cout << "Sorted array: ";
  printArray(arr, length);

  return 0;
}