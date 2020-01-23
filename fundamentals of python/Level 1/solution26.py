#PF-Prac-26
def check_occurence(string):
    #start writing your code here
    if string.casefold().count("jet")==string.casefold().count("mat"):
        return True
    else:
        return False
string="Jet on the Mat but mat is too long"
print(check_occurence(string))
