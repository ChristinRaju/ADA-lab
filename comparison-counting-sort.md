Algorithm: Comparison Counting Sort

Input: Array A[0 … n−1]
Output: Sorted array S[0 … n−1]

1. Initialize count array:
   for i ← 0 to n − 1 do
       Count[i] ← 0

2. Count smaller elements:
   for i ← 0 to n − 2 do
       for j ← i + 1 to n − 1 do
           if A[i] < A[j] then
               Count[j] ← Count[j] + 1
           else
               Count[i] ← Count[i] + 1

3. Place elements in sorted position:
   for i ← 0 to n − 1 do
       S[Count[i]] ← A[i]

4. return S
