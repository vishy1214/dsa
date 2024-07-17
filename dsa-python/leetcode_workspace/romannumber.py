def romanToInt(s: str) -> int:
    roman_dict = {
        "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8,
        "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 500, "D": 500,
        "CM": 900, "M": 1000
    }

    sIdx = 0
    romanChar = ""
    numeric_val = 0
    while (sIdx < len(s)):
        currentRomanChar = s[sIdx]
        temp = romanChar + currentRomanChar
        if (roman_dict.get(temp) != None):
            romanChar = temp
        if(roman_dict.get(temp) == None or sIdx == len(s)-1):
            numeric_val = numeric_val + roman_dict.get(romanChar)
            romanChar = currentRomanChar
        sIdx += 1

    return numeric_val

def romanToInt_superfast( s: str) -> int:

        s = (s.replace("CM", "A").replace("XC", "E")  # 1)
             .replace("IX", "G").replace("CD", "B")
             .replace("XL", "F").replace('IV', "H"))

        rom = {'M': 1000, 'C': 100, 'X': 10, 'I': 1, 'A': 900,  # 2)
               'E': 90, 'G': 9, 'D': 500, 'L': 50, 'V': 5,
               'B': 400, 'F': 40, 'H': 4}

        sum = 0
        for sI in s:
            sum = sum + rom[sI]

        return sum


print(romanToInt("III"))
print(romanToInt_superfast("III"))