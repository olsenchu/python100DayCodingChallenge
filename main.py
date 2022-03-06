print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

combined_name = name1 + name2

combined_name_t_count = int(combined_name.count('t'))
combined_name_r_count = int(combined_name.count('r'))
combined_name_u_count = int(combined_name.count('u'))
combined_name_e_count = int(combined_name.count('e'))
combined_name_true_count = (combined_name_t_count + combined_name_r_count + combined_name_u_count + combined_name_e_count)

combined_name_l_count = int(combined_name.count('l'))
combined_name_o_count = int(combined_name.count('o'))
combined_name_v_count = int(combined_name.count('v'))
combined_name_e_count = int(combined_name.count('e'))
combined_name_love_count = (combined_name_l_count + combined_name_o_count + combined_name_v_count + combined_name_e_count)

love_score = (str(combined_name_true_count) + str(combined_name_love_count))
love_score = int(love_score)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <=50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

