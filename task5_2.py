rating = [8, 7, 6, 4, 4, 2, 2]
new_element = int(input('New rating element '))
if new_element in rating:
    rating.insert(rating.index(new_element), new_element)
else:
    if min(rating) > new_element:
        rating.append(new_element)
    else:
        for elem in rating:
            if elem < new_element:
                break
        rating.insert(rating.index(elem), new_element)

print(rating)
