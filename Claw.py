# [Comments]
# 
# [Author]
# 
# ██████████  █████████   █████████    ████████   ██████████      █████████    ████████ 
#     ██         ███      ███          ███         ███   ███            ███    ███      
#     ██         ███      ███  ▄▄▄▄    ████████    █████████      █████████    ████████ 
#     ██         ███      ███   ███    ███         ███  ███             ███          ███
#     ██      █████████   █████████    ████████    ███    ███     █████████    ████████ 
# 
# Hi I am Tiger 35!
# You might know me from Reddit or Github!
# To do list |help command|
# 
# [Application]
# 
#   █████████   ███           █████     ██           ██         ████████   ████████     █████████   ██████████    ███████   ██████████ 
#  ███          ███         ███   ███   ███         ███         ███        ███    ███      ███          ██       ███   ███   ███   ███ 
#  ███          ███         ███   ███   ███   ███   ███   ▄▄▄   ████████   ███    ███      ███          ██       ███   ███   █████████ 
#  ███          ███         █████████   ███  █████  ███         ███        ███    ███      ███          ██       ███   ███   ███  ███  
#   █████████   █████████   ██     ██   █████     █████         ████████   ████████     █████████       ██        ███████    ███    ███
# 

# Imports
import os
import sys

# Universal Variables
write_mode_encoding = 'utf-8'
read_mode_encoding = 'utf-8'
append_mode_encoding = 'utf-8'
len_mode_encoding = 'utf-8'
Infile_mode_directory_encoding = 'utf-8'
claw_version = "Claw Text Editor Version 1.0.0"

# Title
print("[Claw Text Editor]\n".center(155))

while True:

        terminal = input("""Terminal:- """)

        if terminal == "0" or terminal == "w":

            print()

            try:

                print("[Write Mode]")

                print()

                writefilename = input("Dir:- ")

                with open(writefilename, "w", encoding=write_mode_encoding) as f:
                    
                    print()

                    print("=" * 155)

                    lines_to_write = []

                    while True:
                    
                        write = input("")

                        if write == ":q":

                            print("=" * 155)

                            print(f"\nDid not Save {writefilename}\n")

                            break

                        elif write == ":s":

                            print("=" * 155)

                            f.write("\n".join(lines_to_write))

                            print(f"\nSaved {writefilename} successfully!\n")

                            break
                        else:

                            lines_to_write.append(write)
                
            except Exception:

                print()

                print("=" * 155)

                print()

                print("Error #1 Write Mode failed\n")

                print("=" * 155)

                print()

        elif terminal == "1" or terminal == "q":

            break

        elif terminal == "2" or terminal == "r":

            print()

            try:

                print("[Read Mode]")

                print()

                readfilename = input("Dir:- ")

                print()

                print("=" * 155)

                with open(readfilename, "r", encoding=read_mode_encoding) as f:

                    print(f.read())

                    print("=" * 155)

                    print()

            except:

                print("\nError #2 Read Mode failed\n")

                print("=" * 155)

                print()

        elif terminal == "3" or terminal == "n":

            print()

            try:

                print("[Rename Mode]")

                print()
                
                old_rename = input("Dir:- ")

                print()

                new_rename = input("Replace Dir:- ")

                print()

                os.rename(old_rename,new_rename)

                print()

            except:

                print()

                print("=" * 155)

                print()

                print("Error #3 Rename Mode failed\n")

                print("=" * 155)

                print()

        elif terminal == "4" or terminal == "d":

            print()

            try:

                print("[Delete Mode]")

                print()

                deletefilename = input("Dir:- ")

                print()

                os.remove(deletefilename)

                print("Successfully Deleted!")

                print()

            except:

                print("=" * 155)

                print()

                print("Error #4 Delete Mode failed\n")

                print("=" * 155)

                print()

        elif terminal == "5" or terminal == "ver" or terminal == "version":

            print()

            print(f"{claw_version}")

            print()

        elif terminal == "6" or terminal == "clr" or terminal == "clear":

            os.system('cls' if os.name == 'nt' else 'clear')

            print("[Claw Text Editor]\n".center(155))

        elif terminal == "7" or terminal == "a":

            try:
                
                print()

                print("[Append Mode]")

                print()

                appendfilename = input("Dir:- ")

                with open(appendfilename, "a", encoding=append_mode_encoding) as f:
                    
                    print()

                    print("=" * 155)

                    lines_to_append = []

                    while True:
                    
                        write = input("")

                        if write == ":q":

                            print("=" * 155)

                            print(f"\nDid not Append to {appendfilename}\n")

                            break

                        elif write == ":s":

                            print("=" * 155)

                            f.write("\n".join(lines_to_append) + "\n")

                            print(f"\nAppended to {appendfilename} successfully!\n")

                            break

                        else:

                            lines_to_append.append(write)

            except:

                print()

                print("=" * 155)

                print()

                print("Error #5 Append Mode Failed\n")

                print("=" * 155)

                print()

        elif terminal == "pyver":

            print()

            print(f"{sys.version}")

            print()

        elif terminal == "python":
        
            print()
        
            print(f"{sys.version_info}")
        
            print()

        elif terminal == "eval":

            try:

                print()

                print("[Eval Mode]")

                print()

                evalinput = input()

                print()

                print(eval(evalinput))

                print()

            except:

                print()

                print("=" * 155)

                print()

                print("Error #6 Eval Mode Failed\n")

                print("=" * 155)

                print()

        elif terminal == "len" or terminal == "length":

            try:

                print()

                print("[Len Mode]")

                print()

                len_directory = input("Dir:- ")

                print()

                len_filedata = open(len_directory, "r" , encoding=len_mode_encoding)

                len_readfiledata = len_filedata.read()

                len_readfiledata_nolines = len_readfiledata.replace("\n","")

                len_filedata.close()

                print_length = len(len_readfiledata_nolines)

                if print_length == 1:

                    print(f"Dir:- {len_directory} File contains {print_length} Character")

                    print()

                else:

                    print(f"Dir:- {len_directory} File contains {print_length} Characters")

                    print()

            except:

                print()

                print("=" * 155)

                print()

                print("Error #7 Len Mode Failed\n")

                print("=" * 155)

                print()

        elif terminal == "infile" or terminal == "if":

            try:

                print()

                print("[Infile Mode]")

                print()

                Infile_mode_directory = input("Dir:- ")

                print()

                Infile_mode_stringtofind = input("Find:- ")

                print()

                with open(Infile_mode_directory, "r" , encoding = Infile_mode_directory_encoding) as infile_mode_asfiledir:

                    if Infile_mode_stringtofind in infile_mode_asfiledir.read():

                        print(True)

                    else:

                        print(False)

                print()

            except:

                print()

                print("=" * 155)

                print()

                print("Error #8 Infile Mode Failed\n")

                print("=" * 155)

                print()

        elif terminal == "filesize" or terminal == "fs":

            try:

                print()

                print("[Filesize Mode]")

                print()

                filesize_mode_dir = input("Dir:- ")

                print()

                filesize_mode_size = os.path.getsize(filesize_mode_dir)

                if filesize_mode_size == 1:

                    print(f"{filesize_mode_size} Byte")

                else:

                    print(f"{filesize_mode_size} Bytes")

                print()

            except:

                print()

                print("=" * 155)

                print()

                print("Error #9 Filesize Mode Failed\n")

                print("=" * 155)

                print()

        else:

            print()

            print("=" * 155)

            print()

            print("Error #0 Unknown Command\n")

            print("=" * 155)

            print()