from datetime import datetime
import random

def bubble_sorted_classic(mass_numbers, index = 0):
    start_time = datetime.now()
    while index + 1 != len(mass_numbers):
        if mass_numbers[index] <= mass_numbers[index + 1]:
            index += 1 
            continue
        mass_numbers[index + 1], mass_numbers[index] = mass_numbers[index], mass_numbers[index + 1]    
        if index == 0:
            continue
        index -= 1    
    time = datetime.now() - start_time    
    return time , mass_numbers

mass_numbers = [random.randint(0,1000) for _ in range(1000)]
sort = bubble_sorted_classic(mass_numbers)
