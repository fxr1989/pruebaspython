# [1, 1, 2, 2, 4] -> [1, 2, 4]

def remove_duplicates(some_list):
    withoput_duplicates = []
    for element in some_list:
        if element not in withoput_duplicates:
            withoput_duplicates.append(element)
    return withoput_duplicates

def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(random_list))
    print(list(set(random_list)))

if __name__ == "__main__":
    run()
