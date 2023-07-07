
### Logarithms and Exponents

1.
2 4 8 16 32 (2^5)
64 128 256 512 1024 (2^10)
2048 4096 8192 16384 32768 (2^15)
65536 131072 262144 524288 1048576 (2^20)
2097152 4194304 8388608 16777216 33554432 (2^25)
67108864 134217728 268435456 536870912 1073741824 (2^30)

2. The inverse of expontential. log(n) = x is also n = x^2. For example, log(2) = 10 is also 2 = 10^2.

3. 31 - 28 = 3. 2^3 = 8x larger

4. 1000x larger

5. log(1000)x larger?

6. log(64) = y
2^6 = y^2
2^7 = y^3

7. log(x) = 128
x = 128^2
x = 256

8. log(x/y) = 4
x/y = 4^2
x = 16y

9. log(x * y) = 8
x * y = 8^2 = 64

10. x = 2^8
x = 4^y
2^8 = 2^2y
8 = 2y
4 = y

### Geometric Series
#### 1. What is a geometric series? Give 4 examples of different geometric series. If possible, compute their sum or explain why you can't.

Geometric series is a series of numbers where each "term" (?) except the first is multipliying by the common ratio with its position in the series.
Ratio aka common ratio is fixed, non-zero

Formula for infinite geometric series:
  S = a / (1 - r)

Formula for finite geometric series:
  S = a(1 - r^n) / (1 - r)


Examples:
2, 4, 8, 16, 32
a = 2
r = 4/2 = 2

2, 6, 18, 54, 162
a = 2
r = 6/2 = 3

10, 5, 2.5, 1.25, 0.625
a = 10
r = 5/10 = 0.5

4, 6, 9, 13.5, 20.25
a = 4
r = 6/4 = 1.5


#### 2. We say a series "converges" if you can compute the sum. What types of geometric series converge? You don't need to prove it - just describing it is fine. You can also use examples to explain your idea.

When |r| is less than 1, the series converges. Greater, the series diverges. If it's greater than 1 then the numbers keep going up in value so it's going to infinite. Smaller the final terms will be close to 0

#### 3. Compute ​1+2+4+8+16+32+64 as a power of 2 minus an additional term.

2^0 + 2^1 + 2^2 + 2^3 + 2^4 + 2^5 + 2^6

a = 1
r = 2/1 = 2

S = a/(1-r)
S = 1/(1-(1/2))

S = a(1-r^n)/(1-r)
S = 1(1-2^7)/1-2
S = 1-2^7/-1
S = 1-128/-1
S = 127 (2^7 - 1)


#### 4. Compute 64+32+16+8+4+2+1​ as a power of 2 minus an additional term.

2^6 + 2^5 + 2^4 + 2^3 + 2^2 + 2^1 + 2^0

a = 64
r = 32/64 = 1/2
S = a/(1-r)

S = 64/(1-(1/2))
S = 64/(1/2)
S = 128 (2a)

S = a(1-r^n)/(1-r)
S = 64(1-(1/2)^7)/(1-(1/2))
S = 64 - 


#### 5. Compute 1 + 1/2 + 1/4 + 1/8​ 

a = 1
r = (1/2)/1 = 1/2
S = a/(1-r)

S = 1/(1-(1/2))
S = 1/(1/2)
S = 2

S = a(1-r^n)/(1-r)



#### 6. Compute 1 + 1/2 + 1/4 + 1/8 + 1/16 + 1/32​

a = 1
r = (1/2)/1 = 1/2
S = a/(1-r)

S = 1/(1-(1/2))
S = 1/(1/2)
S = 2


#### 7. If you keep adding more terms to the geometric series, what does it look like you get closer to? I.e., what does the series ​1 + 1/2 + 1/4 + 1/8 + ....​ equal?

It will still equal close to 2


#### 8. Now assume the sum goes from 64 down to 0 like this
64+32+16+8+4+2+1+1/2+1/4+1/8.....​ What is this equal to?

127-128

#### 9. Compute  9+90+900+9000 as a power of 10 minus an additional term.




#### 10. What integer does following expression approach? 
9000+900+90+9+9/10 +9/100 +.... . 

10000 because I can tell by adding up 900 + 90 + 9 and that's 999 and it'll never reach 1000. 


#### 11. Compute 54+27+9+3+1​

finite
It should be 81 for first number?

a = 54
r = 0.5

#### 12. Generaling a sum of powers of 3, estimate 1+3+9+....+3^n​. 
  ##### a. What is the sum in terms of big O notation?
  ##### b. Try to get an exact answer in terms of n



### Runtime Analysis      


#### 1. What is the runtime to iterate through a list of size n​?
O(n)


#### 2. Write a function that runs in each of the following runtimes O(1), O(log n), O(n), O(n log n), O(n^2), O(n^2 log n), O(n (log n)^2), O(2^n).


def static(k):
  return k + 1

def log_n(k):



#### 3. When we say an algorithm has O(1) runtime, what does that say about the runtime in terms of the input?
The input doesn't make a difference


#### 4. How can you calculate the runtime when operations are nested? 

Nested operations multiply with one another


#### 5. Give an example of an algorithm or write a function with O(1) runtime.


#### 6. Given a table of code runtime (input size/runtime), can you determine what order of growth these functions have? Hint: Applying the doubling principle.


### Explain and Analyze Code