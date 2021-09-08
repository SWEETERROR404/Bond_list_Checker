import os,requests,re

line = "-------------------------------------"
print(f"{line}\nBond List Checker\nCreated by Sweeterror404\n{line}")

try:
    os.remove("Downloaded_lists/.temp")
except:
    pass

try:
    os.mkdir("Downloaded_lists")
except:
    pass

try:
    os.mkdir("my_Bond_lists")
except:
    pass

user_input = input("Press D for Downlaod list \nPress C for Check list \n")

#Download Function
def Download():
    # error if Downloaded_lists folder not exist
    try:
        os.mkdir("Downloaded_lists")
    except:
        pass

    with open("Downloaded_lists/.temp","w") as tmp:
        tmp.write("Dont Deleted this file")

    link = input("\ngo to http://savings.gov.pk/download-draws/ \nand select draw list and copy link and paste Here :- ")
    x = requests.get(link)

    command = None
    while True:
        file_name = input("Enter the name of the list :- ")

   # check file name are already exist or not
        for i in os.listdir("Downloaded_lists"):
            if i == file_name+".txt":
                print(f"--> {file_name} <-- file are already Exist Please type another Name !")
                command = 1
            elif i != file_name+".txt":
                command = 0

        if command == 0:
        # Saved list
            with open(f"Downloaded_lists/{file_name}.txt", "wb") as f:
                f.write(x.content)
                print(f"List are Downloaded Sucessfully in Downloaded_lists/{file_name}.txt")
                break
    os.remove("Downloaded_lists/.temp")

#Check Function
def Check():

    try:
        os.remove("Downloaded_lists/.temp")
    except:
        pass

    print("Total Lists")
    for i in os.listdir("Downloaded_lists"):
        print(i)

    command = None
    print("\n")
    while True:
        downloaded_file = input("Type file Name ")

        for i in os.listdir("Downloaded_lists"):
            if i in downloaded_file+".txt":
                print(i+" file are Selected")


                # bond list
                print("\nTotals Bond lists ")
                for i in os.listdir("my_Bond_lists"):
                    print(i)

                user_input = input("Type your bond lists :- ")

                for my_list in os.listdir("my_Bond_lists"):
                    if user_input+".txt" in my_list:
                        print(my_list+" file are Selected ")

                        output = []
                        with open(f"Downloaded_lists/{downloaded_file}.txt", "r") as f:
                            r = f.read()
                            t = sorted(re.findall(r"\d{6}", r))
                            with open(f'my_Bond_lists/{user_input}.txt', "r") as rw:
                                bond = rw.read()
                                for x in t:
                                    if x in bond:
                                        output.append(x)

                        if output != []:
                            print("\nFound")
                            print(output)
                        else:
                            print("\nNot Match")

                command = 0
            else:
                command = 1

        if command == 0:
            break
        else:
            print("Please Type Correct Name !")

if len(os.listdir("Downloaded_lists")) == 0:
    print("Download Folder Empty Please Download Files")
    Download()

if len(os.listdir("my_Bond_lists")) == 0:
    print("my_Bond_lists Folder Empty Please add your Bond list Files")

if user_input == "d":
    Download()

elif user_input == "c":
    Check()