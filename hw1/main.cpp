// compile with g++ -std=c++11 main.cpp

#include <chrono>
#include <fstream>
#include <iostream>
#include <limits.h>
#include <random>
#include <vector>

std::vector<int> generateRandomArray(int n = 10)
{
  std::random_device rd;
  std::mt19937 gen(rd());
  std::uniform_int_distribution<> dis(-INT_MIN, INT_MAX);

  std::vector<int> result(n);

  std::generate(result.begin(), result.end(), std::bind(dis, gen));

  return result;
}

void insertionSort(std::vector<int> &arr)
{
  int n = arr.size();

  for (int i = 1; i < n; ++i)
  {
    int key = arr[i];
    int j = i - 1;

    while (j >= 0 && arr[j] > key)
    {
      arr[j + 1] = arr[j];
      j = j - 1;
    }

    arr[j + 1] = key;
  }
}

std::vector<int> linspace(int start, int end, int numPoints)
{
  std::vector<int> result;
  double stepSize = static_cast<double>(end - start) / (numPoints - 1);

  for (int i = 0; i < numPoints; ++i)
  {
    int value = static_cast<int>(std::round(start + i * stepSize));
    result.push_back(value);
  }

  return result;
}

void measureInsertionSort(int n, std::vector<std::pair<int, long long>> &runtimes)
{
  std::vector<int> arr = generateRandomArray(n);
  // std::cout << "Random Array: ";
  // for (const auto &element : arr)
  // {
  //   std::cout << element << " ";
  // }
  // std::cout << std::endl;

  auto start = std::chrono::high_resolution_clock::now();

  insertionSort(arr);

  auto end = std::chrono::high_resolution_clock::now();
  auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
  std::cout << "n = " << n << ", Execution time: " << duration.count() << " milliseconds" << std::endl;
  runtimes.push_back(std::make_pair(n, duration.count()));

  // std::cout << "Sorted Array: ";
  // for (const auto &element : arr)
  // {
  //   std::cout << element << " ";
  // }
  // std::cout << std::endl;
}

void writePairsToCSV(const std::vector<std::pair<int, long long>> &runtimes, const std::string &filename)
{
  std::ofstream file(filename);

  if (!file.is_open())
  {
    std::cout << "Failed to open the file: " << filename << std::endl;
    return;
  }

  for (const auto &pair : runtimes)
  {
    file << pair.first << ',' << pair.second << '\n';
  }

  file.close();

  std::cout << "Runtime written to " << filename << " successfully." << std::endl;
}

int main()
{
  int start = 100;
  int end = 100000;
  int numPoints = 30;
  std::vector<std::pair<int, long long>> runtimes;
  std::vector<int>
      values = linspace(start, end, numPoints);

  for (int n : values)
  {
    measureInsertionSort(n, runtimes);
  }

  std::string filename = "result.csv";

  writePairsToCSV(runtimes, filename);

  return 0;
}