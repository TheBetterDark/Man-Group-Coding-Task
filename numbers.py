def find_most_common(list):
    return max(list, key=list.count)

def find_missing(list, min, max):
    missing_numbers = []
    
    for num in range(min, max):
        if not num in list:
            missing_numbers.append(num)
        
    return missing_numbers
   
    
def main():
    numbers = []
    f = open("numbers.txt", "r")
    
    # Iterate through each line in text file and storing in a list as a interget datatype
    for line in f: 
        x = f.readline()
        y = x.split()
        numbers.append(int(y[0]))
        
    f.close()
    
    print("The digit that appears the most is: " + str(find_most_common(numbers))) # Print which digit appear the most
    print("The missing digits are: " + str(find_missing(numbers, 1, 1563)))   # Print which digit is missing from file


if __name__ == '__main__':
    main()
