# n customers are given ratings
# Each customer needs a minimum ratings a[n]
# All the ratings must be unique
# And the sum must be minimum

n = input("Enter the number of customers\n")

def min_rating(n):
    a = []
    rating[9] = 0
    sum = 0
    for i in range(n):
        rate = input(f"Enter the rating of customer {i+1}\n")
        if rating[rate] != 1:
            rating[rate] = 1
        else:
            rate += 1
            rating[rate] = 1
        a[i]=rate
        sum += a[i]
    return sum

print(min_rating(n))
