def find_most_common(list):
    return max(list, key=list.count)


def find_least_common(list):
    return min(list, key=list.count)


def find_containing_green(list):
    count = 0

    for colour in list:
        new_list = []

        for colour in colour.split(","):
            new_list.append(colour)

        if any([x in "GREEN" for x in new_list]) and not any([x in "BLUE" for x in new_list]):
            count += 1

    return count


def find_repeated_colours(list):
    count = 0

    for colour in list:
        new_list = []

        for colour in colour.split(","):
            new_list.append(colour)

        if new_list.count(new_list[0]) == len(new_list):
            count += 1

    return count


def find_different_colours(list):
    count = 0

    for colour in list:
        new_list = []

        for colour in colour.split(","):
            new_list.append(colour)

        if (len(set(new_list)) == len(new_list)):
            count += 1

    return count


def find_alphabetical_order(list):
    count = 0

    for colour in list:
        new_list = []

        for colour in colour.split(","):
            new_list.append(colour)

        new_list1 = new_list[:]
        new_list1.sort()

        if (new_list1 == new_list):
            count += 1

    return count


def main():
    colours = []
    colours_without_commas = []
    f = open("colours.txt", "r")

    # Iterate through each line in text file and storing in a list as a string
    for line in f:
        x = f.readline()
        y = x.split()
        colours.append(y[0])

        for colour in x.split(","):
            colours_without_commas.append(colour)

    f.close()

    # Print the colour that appears the most
    print("The colour that appears the most is: " + find_most_common(colours_without_commas))
    
    # Print the colour that appears the least
    print("The colour that appears the least is: " + find_least_common(colours_without_commas))
    
    # Print the amount lines that contain green but not blue
    print("The amount of lines that contain green but not blue is: " + str(find_containing_green(colours)))
    
    # Print the of amount lines that have the same colour that is repeated three times
    print("The amount of lines that have the same colour that is repeated three times is: " + str(find_repeated_colours(colours)))
    
    # Print the amount of lines that have three different colours present
    print("The amount of lines that have three different colours present is: " + str(find_different_colours(colours)))
    
    # Print the amount of lines that have colours in alphabetical order
    print("The amount of lines that have colours in alphabetical order is: " + str(find_alphabetical_order(colours)))


if __name__ == '__main__':
    main()
