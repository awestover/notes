#include <iostream>
#include <pthread.h>
#include <time.h>

#define ARR_MAX 200000
#define THREAD_MAX 4 // I am not sure if this is really the max, but I think that it is on my computer

// high and low are both included

using namespace std;

int arr[ARR_MAX];
int part = 0;

void pArr(int arr[], int N) {
  for (int i = 0; i < N; i++) {
    printf("%d ", arr[i]);
  }
  printf(" \n");
}

void merge(int low, int mid, int high) {
  int temp[high-low+1];
  int li = low; int hi = mid+1;
  for (int i = low; i <= high; i++) {
    if (li > mid) {
      for (int j = i; j <= high; j++) {
        temp[j-low] = arr[hi++];
      }
      break;
    }
    if (hi > high) {
      for (int j = i; j <= high; j++) {
        temp[j-low] = arr[li++];
      }
      break;
    }
    if(arr[li] <= arr[hi])
      temp[i-low] = arr[li++];
    else
      temp[i-low] = arr[hi++];
  }
  for (int i = low; i <= high; i++) {
    arr[i] = temp[i-low];
  }
}

void merge_sort(int low, int high) {
  int mid = low + (high-low)/2;
  if (low < high) {
    merge_sort(low, mid);
    merge_sort(mid+1,high);
    merge(low, mid, high);
  }
}

void* merge_sort(void* arg) {
  int thread_part = part++;

  int low = thread_part*(ARR_MAX/4);
  int high = (thread_part + 1) * (ARR_MAX / 4) - 1;

  int mid = low + (high-low)/2;
  std::cout << "thread running merge sort" << '\n';
  if (low < high) {
    merge_sort(low, mid);
    merge_sort(mid+1, high);
    merge(low,mid,high);
  }
  return NULL;
}

int main() {

  srand(time(NULL)); // seed for random numbers

  for (int i = 0; i < ARR_MAX; i++) {
    arr[i] = rand()%10000;
  }

  std::cout << "Initial Array (first 10 elements)" << '\n';
  // pArr(arr, ARR_MAX);
  pArr(arr, 10);
  clock_t t1, t2;
  t1 = clock();
  pthread_t threads[THREAD_MAX];

  // create the threads
  for (int i = 0; i < THREAD_MAX; i++) {
    pthread_create(&threads[i], NULL, merge_sort, (void*)NULL);
    // pthread_create(thread: address of thread, attr: set thread attributes (can be NULL), start_routine: the routine the thread will execute once created, arg: arguments to start routine (can be NULL));
    std::cout << "thread created" << '\n';
  }

  // join all of the threads
  for (int i = 0; i < THREAD_MAX; i++) {
    // this stops the thread from being used for other purposes I think...
    pthread_join(threads[i], NULL);
  }

  // merge the 4 separate parts
  int elow, ehigh, emid;
  elow = 0; ehigh = ARR_MAX/2 - 1; emid = elow + (ehigh - elow)/2;
  merge(elow, emid, ehigh);
  elow = ARR_MAX/2; ehigh = ARR_MAX-1; emid = elow + (ehigh - elow)/2;
  merge(elow, emid, ehigh);
  elow = 0; ehigh = ARR_MAX-1; emid = elow + (ehigh - elow)/2;
  merge(elow, emid, ehigh);

  t2 = clock();
  std::cout << "Sorted Array (first 10 elements) (shold be all 0)" << '\n';
  // pArr(arr, ARR_MAX);
  pArr(arr, 10);
  std::cout << "Time taken: " << (t2 - t1) / (double)CLOCKS_PER_SEC << '\n';

  return 0;
}
