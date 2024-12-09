def mirror_letter(letter):
    mirror_map = {'a' : 'ɒ', 'b' : 'd', 'c' : 'ɔ', 'd' : 'b', 'e' : 'ɘ', 'f' : 'ʇ', 
'g' : 'ϱ', 'h' : 'ʜ', 'i' : 'i', 'j' : 'į', 'k' : 'ʞ', 'l' : 'l', 
'm' : 'm', 'n' : 'n', 'o' : 'o', 'p' : 'q', 'q' : 'p', 'r' : 'ɿ', 
's' : 'ƨ', 't' : 'Ɉ', 'u' : 'υ', 'v' : 'v', 'w' : 'w', 'x' : 'x', 
'y' : 'γ', 'z' : 'z', 'A' : 'A', 'B' : 'Ƃ', 'C' : 'Ɔ', 'D' : 'ᗡ', 'E' : 'Ә', 'F' : 'ᆿ', 
'G' : 'Ǝ', 'H' : 'H', 'I' : 'I', 'J' : 'Ⴑ', 'K' : 'ﻼ', 'L' : '⅃', 
'M' : 'M', 'N' : 'И', 'O' : 'O', 'P' : 'Գ', 'Q' : 'Ϙ', 'R' : 'Я', 
'S' : 'Ƨ', 'T' : 'T', 'U' : 'U', 'V' : 'V', 'W' : 'W', 'X' : 'X', 
'Y' : 'Y', 'Z' : 'Z'}
    return mirror_map.get(letter, letter)
def mirror_image_string(string):
    mirrored_string = "".join(mirror_letter(char) for char in string)
    return mirrored_string
input_string = input("Enter a string to mirror: ")
mirror_string = mirror_image_string(input_string)
print(f"The mirrored string is: {mirror_string}")