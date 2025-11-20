# 3-4
Guest_list = ['Michael Jordan', 'Kobe Bryant', "Majic Johnson"]
print(f"Hey {Guest_list[0]}, you are invited to my dinner party. RSVP ")
print(f"Hey {Guest_list[1]}, you are invited to my dinner party. RSVP ")
print(f"Hey {Guest_list[2]}, you are invited to my dinner party. RSVP ")

# 3-5
# One guest cant make it 
cant_make_it = 'Kobe Bryant'
print(f"\nUnfortunately {cant_make_it} cannot make it to dinner")
Guest_list[1] = 'Lebron James' 
print(f"\nHey {Guest_list[0]}, Unfortunately {cant_make_it} cannot make it to dinner. Despite that, you  are still invited to dinner")
print(f"\nHey {Guest_list[1]}, Unfortunately {cant_make_it} cannot make it to dinner. Despite that, you  are still invited to dinner")
print(f"\nHey {Guest_list[2]}, Unfortunately {cant_make_it} cannot make it to dinner. Despite that, you  are still invited to dinner")


# 3-6
# More Guests
print("\nGreat News!, I found a bigger dinner table ") 
Guest_list.insert(0, "Shaquille O'Neal")
Guest_list.insert(len(Guest_list)//2, "Tim Duncan")
Guest_list.append("Kevin Durant")

print(f"Dear {Guest_list[0]}, you are invited to dinner")
print(f"Dear {Guest_list[1]}, you are invited to dinner")
print(f"Dear {Guest_list[2]}, you are invited to dinner")
print(f"Dear {Guest_list[3]}, you are invited to dinner")
print(f"Dear {Guest_list[4]}, you are invited to dinner")
print(f"Dear {Guest_list[5]}, you are invited to dinner")