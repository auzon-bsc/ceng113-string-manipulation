# -*- coding: utf-8 -*-
"""
@author: Oğuzhan Özer
studentID: 260201039
"""
# =============================================================================
#  Checks given nucleic acid valid or not
#  You must enter a DNA or RNA list for type_of_NA
#  It checks first string and recurse rest of the string
# =============================================================================
def is_NA_valid(NA, type_of_NA):
       
    if NA[0] not in type_of_NA:
        return False
    elif len(NA) > 1:
        return is_NA_valid(NA[1:], type_of_NA)
    else:
        return True
# =============================================================================
#  - Checks it is DNA, RNA or invalid
#  - It calls is_NA_valid function for checking the type of nucleic acid
#  - If there is a specific base in sequence (like T for DNA) the function 
#  gonna detect is either DNA or RNA
#  - If there is not a specific base, then it could be either DNA or RNA      
# ============================================================================= 
def is_DNA_RNA_or_invalid(NA):
    DNA_bases = ["A", "G", "C", "T"]
    RNA_bases = ["A", "G", "C", "U"]
    is_DNA = is_NA_valid(NA, DNA_bases)
    is_RNA = is_NA_valid(NA, RNA_bases)
    
    if is_DNA == False and is_RNA == False:
        return "It is invalid"    
    elif NA[0] == "T":
        return "It is DNA"
    elif NA[0] == "U":
        return "It is RNA"
    elif len(NA) > 1:
        return is_DNA_RNA_or_invalid(NA[1:])
    
    return "It can be DNA or RNA"
# =============================================================================
# - The working method of this function is similar to first two but if the 
# base is purine it will change to the pyrimidine and vice versa
# =============================================================================
def complementary_of_DNA(DNA_sequence):
    purine_bases = ["A", "G"]
    pyrimidine_bases = ["T", "C"]
	
    if len(DNA_sequence) == 1:    
        if DNA_sequence[0] in purine_bases:
            index_of_base = purine_bases.index(DNA_sequence[0])
            complementary = pyrimidine_bases[index_of_base]
            return complementary
        elif DNA_sequence[0] in pyrimidine_bases:
            index_of_base = pyrimidine_bases.index(DNA_sequence[0])
            complementary = purine_bases[index_of_base]            
            return complementary
    else:
        comp_DNA_first = complementary_of_DNA(DNA_sequence[0])
        comp_DNA_rest = complementary_of_DNA(DNA_sequence[1:])
        return comp_DNA_first + comp_DNA_rest
# =============================================================================
# - It sorts the short sequence and long sequence then if there is a difference
# between two bases in same place then it add 1 to result if there is not then
# it add 0 and this will not incement the difference counter
# =============================================================================
def difference(short, long):
    size_of_short = len(short)
    size_of_long = len(long)
    
    if size_of_short > size_of_long:
        temp = long
        long = short
        short = temp
    
    if len(short) == 1:
        if short != long:
            return 1
        else:
            return 0
    else:
        return difference(short[0], long[0]) + difference(short[1:], long[1:])
# =============================================================================
# - It takes choices from user and depending on these choices our other
# functions will called
# =============================================================================
def main():    
    user_input = "-1"

    while True:
        print("""
Enter 1 to check nucleic acid is valid or not
Enter 2 to check nucleic acid is a DNA, RNA or invalid
Enter 3 to generate complementary of any DNA
Enter 4 to find difference between two nucleic acid
Enter 0 to exit
              """)
        
        user_input = input("Your choice: ")
        valid_inputs = ["1", "2", "3", "4"]
        
        if user_input == "0":
            break        
        
        elif user_input not in valid_inputs:
            print("Enter a valid choice!")
            continue
        
        if user_input == "1":
            DNA_bases = ["A", "G", "C", "T"]
            RNA_bases = ["A", "G", "C", "U"]
            input_NA = input("Nucleic acid: ")
            is_DNA = is_NA_valid(input_NA, DNA_bases)
            is_RNA = is_NA_valid(input_NA, RNA_bases)
            
            if is_DNA == True or is_RNA == True:
                print("It is valid")
            else:
                print("It is invalid")
        
        elif user_input == "2":
            input_NA = input("Nucleic acid: ")
            print(is_DNA_RNA_or_invalid(input_NA))
        
        elif user_input == "3":
            DNA_bases = ["A", "G", "C", "T"]
            input_NA = input("DNA sequence: ")
            if is_NA_valid(input_NA, DNA_bases) == True:
                print(complementary_of_DNA(input_NA))
            else:
                print("This is not a valid DNA sequence")
        
        else:
            input_NA1 = input("First nucleic acid: ")
            input_NA2 = input("Second nucleic acid: ")
            NA1_valid = is_DNA_RNA_or_invalid(input_NA1)
            NA2_valid = is_DNA_RNA_or_invalid(input_NA2)
            if NA1_valid == "It is invalid" or NA2_valid == "It is invalid":
                print("One of them or both are not a valid nucleic acid")
            else:
                print(difference(input_NA1, input_NA2))

main()