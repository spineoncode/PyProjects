powers = [5, 6, 7, 8, 4]
mini = 0
maxi = 0
for power in powers:
    if mini == 0 and maxi == 0:
        mini, maxi = power, power
    else:
        mini = min(mini, power)
        maxi = max(maxi, power)
    print(mini, maxi)

# Problem:
# You are a Pokémon trainer. Each Pokémon has its own power, described by a positive integer value. As you travel, you watch Pokémon and you catch each of them. After each catch, you have to display maximum and minimum powers of Pokémon caught so far. You must have linear time complexity. So sorting won’t help here. Try having minimum extra space complexity.