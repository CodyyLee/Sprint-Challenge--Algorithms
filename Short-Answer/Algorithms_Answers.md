#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)

The while loop is directly impacted by the length of the input 'n' so it is O(n). in the loop is O(1), so it's O(n + 1). Simplified it becomes O(n).

b) O(nlog(n))

The for loop is directly impacted by the length of the input 'n' so it is O(n). The while loop is spliting by multiplying J by 2 so it uses the 'divide and conquor' kind of algorithm making it O(log(n)). So bringing them both together would make the entire function O(nlog(n)).

c) O(n^2)

## Exercise II

start = 0
middle = (start + end) // 2
end = len(n) - 1

while True:
  if difference of position in start and middle is 1 or end and middle is 1:
    not found
  else if middle is f:
    return f
  else if middle is > f:
    make end = middle
  else:
    make start = middle


I THINK IT IS O(log n) ?
