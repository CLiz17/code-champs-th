# n customers are given ratings
# Each customer needs a minimum ratings a[n]
# All the ratings must be unique
# And the sum must be minimum

n = int(input("Enter the number of customers\n"))

def min_rating(n):
    rating = [0]*10
    sum = 0
    for i in range(n):
        rate = int(input(f"Enter the rating of customer {i+1}\n"))
        while rating[rate] == 1:
            rate += 1
        rating[rate] = 1
        sum += rate
    return sum

print(min_rating(n))
