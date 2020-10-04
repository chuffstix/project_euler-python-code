def sum_of_squares(n):
    sum_squares = 0
    for i in range(1, n+1):
        sum_squares += i**2
    return sum_squares


def square_of_sum(n):
    square_sum = 0
    for i in range(1, n+1):
        square_sum += i
    return square_sum**2
