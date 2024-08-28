class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_pair = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        lista = list(s)
        roman_list = []
        i = 0
        while i < len(lista):
            if i + 1 < len(lista) and lista[i] + lista[i+1] in roman_pair:
                roman_list.append(roman_pair[lista[i] + lista[i+1]])
                i+=2
            else:
                roman_list.append(roman[lista[i]])
                i+=1

        return sum(roman_list)
