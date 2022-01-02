
def get_numbers_as_words(upper_limit):
    numbers_to_words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
                 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
                11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
                15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', \
                19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', \
                50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', \
                90: 'ninety'}

    numbers_as_letters = []

    for number in range(1,upper_limit):
        if len(str(number)) == 2:
            if str(number)[0] == '1' or str(number)[-1] == '0':
                numbers_as_letters.append(numbers_to_words[number])
            else:
                numbers_as_letters.append(numbers_to_words[(number//10)*10] + \
                                           numbers_to_words[number%10])
        elif len(str(number)) == 3:
            if str(number)[1] == '0' and str(number)[2] == '0':
                numbers_as_letters.append(numbers_to_words[number//100] + 'hundred')
            elif str(number)[-1] == '0' or str(number)[1] == '1' or str(number)[1] == '0':
                numbers_as_letters.append(numbers_to_words[number//100] + 'hundredand' \
                                              + numbers_to_words[number%100])
            else:
                numbers_as_letters.append(numbers_to_words[number//100] + 'hundredand' \
                                          + numbers_to_words[(number%100//10)*10] + \
                                          numbers_to_words[number%10])
        elif len(str(number)) == 4:
            numbers_as_letters.append('onethousand')
        else:
            numbers_as_letters.append(numbers_to_words[number])

    return numbers_as_letters

if __name__ == '__main__':
    nums = get_numbers_as_words(1001)
    print(sum([len(e) for e in nums]))    
