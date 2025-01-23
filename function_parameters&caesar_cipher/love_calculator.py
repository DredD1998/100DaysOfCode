def calculate_love_score(name1, name2):

    true_letters = "TRUE"
    love_letters = "LOVE"
    
 
    def count_letters(name, letters):
        count = 0
        name = name.upper() 
        for letter in letters:
            count += name.count(letter)
        return count
    

    true_count1 = count_letters(name1, true_letters)
    true_count2 = count_letters(name2, true_letters)
    love_count1 = count_letters(name1, love_letters)
    love_count2 = count_letters(name2, love_letters)
    

    true_total = true_count1 + true_count2
    love_total = love_count1 + love_count2
    

    love_score = int(str(true_total) + str(love_total))
    

    print(love_score)


calculate_love_score("Hirak", "Supriya")
