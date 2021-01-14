import csv
import pandas as pd


names = ["francis", "kelynn", ""]

def convert_csv(file):
    df = pd.read_csv(file)
    name_column = df["Name"]

    return name_column

def scan_names(column):
    names = ["josh", "raph", "elton", "francis", "kelly l", "kelly c", "kaitlyn", "baron", "michelle", "young", "brandon", "kelynn", "sharon", "hy", "jon", "vivi", "lisa", "reyna", "henry", "prad", "julie", "tanya", "nguyen"]

    for name in reversed(names):
        for name_resp in column:
            if name in name_resp.lower():
                names.remove(name)
                break

    return(names)

if __name__ == "__main__":
    name_col = None
    print("Hello, welcome to the SASE Name Checker! Use this tool to check if a name is missing from a form.")

    birthday = input("Is this for a birthday? [Y/N] ")

    if birthday.lower() == "y":
        name = input("Who's birthday is it? ")

        try:
            name_col = convert_csv("C:\\Users\\bryan\\Downloads\\Birthday Card for "+name.capitalize()+" (Responses) - Form Responses 1.csv")

        except:
            print("Oops, couldn't find that file!")

    else:
        filepath = input("Enter the file path to the form: ")

        try:
            name_col = convert_csv(filepath)

        except:
            print("Oops, couldn't find that file!")


    names_list = scan_names(name_col)
    print("The following people have not filled out the form yet: ")
    print(*names_list, sep = ", ")
