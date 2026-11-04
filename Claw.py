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
import pathlib
import shutil

# Universal Variables

claw_version = "Claw Text Editor Version 1.0.1"
main_loop_is_running = True
write_mode_encoding = 'utf-8'
read_mode_encoding = 'utf-8'
append_mode_encoding = 'utf-8'
len_mode_encoding = 'utf-8'
infile_mode_directory_encoding = 'utf-8'
replx_mode_encoding_read = 'utf-8'
replx_mode_encoding_write = 'utf-8'
page_divider_border_char = "="
page_divider_border_num = 155
claw_banner_center_location = 155
claw_banner_title_use_ansicode_yes = False
claw_banner_title_use_ansicode = "\033[32m"
claw_banner_title = "[Claw Text Editor]\n"
color_ansi_terminal_yes = False
colorcode_ansi_terminal = "\033[91m"
terminal_prompt_text = "Terminal:- "
dir_terminal_prompt_text = "Dir:- "
ls_dir_banner_divider_border_char = "="
ls_dir_banner_divider_border_num = 155
ask_for_delete_confirmation = True
ask_for_delete_confirmation_input_textprompt = "Are You Sure That You Want To Delete:- "
ask_for_delete_confirmation_input_dir_separaterright = "["
ask_for_delete_confirmation_input_dir_separaterleft = "]"
color_ansiescapecode_warning_for_delete_confirmation = "\033[91m"
mkdir_successful_text = "Directory Successfully Created at:- "
dir_successfully_deleted = "Directory Successfully Deleted!"

# Title

# Check for ANSI Escape Code for title

if claw_banner_title_use_ansicode_yes == False:

    print(f"{claw_banner_title}".center(claw_banner_center_location))

else:

    print(f"{claw_banner_title_use_ansicode}{claw_banner_title}\033[0m".center(claw_banner_center_location))

try:

    # Main Loop

    while main_loop_is_running:

            # Check for ANSI Escape Code for terminal prompt

            if color_ansi_terminal_yes == False:

                terminal = input(f"{terminal_prompt_text}")

            else:

                terminal = input(f"{colorcode_ansi_terminal}{terminal_prompt_text}\033[0m")

            # Check terminal input

            if terminal == "0" or terminal == "w" or terminal == "write":

                print()

                try:

                    print("[Write Mode]")

                    print()

                    writefilename = input(f"{dir_terminal_prompt_text}")

                    with open(writefilename, "w", encoding = write_mode_encoding) as f:
                        
                        print()

                        print(page_divider_border_char * page_divider_border_num)

                        lines_to_write = []

                        while True:
                        
                            write = input("")

                            if write == ":q":

                                print(page_divider_border_char * page_divider_border_num)

                                print(f"\nDid not Save {writefilename}\n")

                                break

                            elif write == ":s":

                                print(page_divider_border_char * page_divider_border_num)

                                f.write("\n".join(lines_to_write))

                                print(f"\nSaved {writefilename} successfully!\n")

                                break
                            else:

                                lines_to_write.append(write)
                    
                except Exception:

                    print()

                    print(page_divider_border_char * page_divider_border_num)

                    print()

                    print("Error #1 Write Mode failed\n")

                    print(page_divider_border_char * page_divider_border_num)

                    print()

            elif terminal == "1" or terminal == "q" or terminal == "quit":

                try:

                    break

                except Exception:

                    print()

                    print(page_divider_border_char * page_divider_border_num)

                    print()

                    print("Error #15 Failed to Exit!\n")

                    print(page_divider_border_char * page_divider_border_num)

                    print()

            elif terminal == "2" or terminal == "r" or terminal == "read":

                print()

                try:

                    print("[Read Mode]")

                    print()

                    readfilename = input(f"{dir_terminal_prompt_text}")

                    print()

                    print(page_divider_border_char * page_divider_border_num)

                    with open(readfilename, "r", encoding=read_mode_encoding) as f:

                        print(f.read())

                        print(page_divider_border_char * page_divider_border_num)

                        print()

                except Exception:

                    print("\nError #2 Read Mode failed\n")

                    print(page_divider_border_char * page_divider_border_num)

                    print()

            elif terminal == "3" or terminal == "n" or terminal == "rename":

                try:

                    print()

                    print("[Rename Mode]")

                    print()
                    
                    old_rename = input(f"{dir_terminal_prompt_text}")

                    print()

                    new_rename = input("Replace Dir:- ")

                    print()

                    os.rename(old_rename,new_rename)

                    print()

                except Exception:

                    print()

                    print(page_divider_border_char * page_divider_border_num)

                    print()

                    print("Error #3 Rename Mode failed\n")

                    print(page_divider_border_char * page_divider_border_num)

                    print()

            elif terminal == "4" or terminal == "d" or terminal == "delete":

                print()

                try:

                    print("[Delete Mode]")

                    print()

                    deletefilename = input(f"{dir_terminal_prompt_text}")

                    if ask_for_delete_confirmation == True:

                        while True:

                            print()

                            print(f"{color_ansiescapecode_warning_for_delete_confirmation}|Following action is irreversible|\033[0m")

                            print()

                            print("y for yes | n for no")

                            print()

                            ask_for_delete_confirmation_input = input(f"{ask_for_delete_confirmation_input_textprompt}{ask_for_delete_confirmation_input_dir_separaterright}{deletefilename}{ask_for_delete_confirmation_input_dir_separaterleft}:- ").lower().strip()

                            if ask_for_delete_confirmation_input == "n" or ask_for_delete_confirmation_input == "no":

                                print()

                                print(f"{deletefilename} Not Deleted!")

                                print()

                                break

                            elif ask_for_delete_confirmation_input == "y" or ask_for_delete_confirmation_input == "yes":

                                print()

                                os.remove(deletefilename)
                                
                                print(f"Successfully Deleted {deletefilename}!")
                                
                                print()

                                break

                            else:

                                continue

                    else:

                        print()

                        os.remove(deletefilename)

                        print(f"Successfully Deleted {deletefilename}!")

                        print()

                except Exception:

                    print(page_divider_border_char * page_divider_border_num)

                    print()

                    print("Error #4 Delete Mode failed\n")

                    print(page_divider_border_char * page_divider_border_num)

                    print()

            elif terminal == "5" or terminal == "version":

                try:

                    print()

                    print(f"{claw_version}")

                    print()

                except Exception:

                    print()

                    print(page_divider_border_char * page_divider_border_num)

                    print()

                    print("Error #16 Failed to Print Version\n")

                    print(page_divider_border_char * page_divider_border_num)

                    print()

            elif terminal == "6" or terminal == "clr" or terminal == "clear" or terminal == "cls":

                try:

                    os.system('cls' if os.name == 'nt' else 'clear')

                    # Check for ANSI Escape Code after clearing terminal

                    if claw_banner_title_use_ansicode_yes == False:

                        print(f"{claw_banner_title}".center(claw_banner_center_location))

                    else:

                        print(f"{claw_banner_title_use_ansicode}{claw_banner_title}\033[0m".center(claw_banner_center_location))

                except Exception:

                    print()

                    print(page_divider_border_char * page_divider_border_num)

                    print()

                    print("Error #17 Clearing Screen with Banner Failed\n")

                    print(page_divider_border_char * page_divider_border_num)

                    print()

            elif terminal == "6." or terminal == "clr." or terminal == "clear." or terminal == "cls.":

                try:

                    os.system('cls' if os.name == 'nt' else 'clear')

                except Exception:

                    print()

                    print(page_divider_border_char * page_divider_border_num)

                    print()

                    print("Error #18 Clearing Screen Failed\n")

                    print(page_divider_border_char * page_divider_border_num)

                    print()

            elif terminal == "7" or terminal == "a" or terminal == "append":

                try:
                    
                    print()

                    print("[Append Mode]")

                    print()

                    appendfilename = input(f"{dir_terminal_prompt_text}")

                    with open(appendfilename, "a", encoding=append_mode_encoding) as f:
                        
                        print()

                        print(page_divider_border_char * page_divider_border_num)

                        lines_to_append = []

                        while True:
                        
                            write = input("")

                            if write == ":q":

                                print(page_divider_border_char * page_divider_border_num)

                                print(f"\nDid not Append to {appendfilename}\n")

                                break

                            elif write == ":s":

                                print(page_divider_border_char * page_divider_border_num)

                                f.write("\n".join(lines_to_append) + "\n")

                                print(f"\nAppended to {appendfilename} successfully!\n")

                                break

                            else:

                                lines_to_append.append(write)

                except Exception:

                    print()

                    print(page_divider_border_char * page_divider_border_num)

                    print()

                    print("Error #5 Append Mode Failed\n")

                    print(page_divider_border_char * page_divider_border_num)

                    print()

            elif terminal == "python":

                try:

                    print()

                    print(f"{sys.version}")

                    print()

                except Exception:

                    print()

                    print(page_divider_border_char * page_divider_border_num)

                    print()

                    print("Error #19 Printing Python Metadata Failed\n")

                    print(page_divider_border_char * page_divider_border_num)

                    print()

            elif terminal == "pyver":

                try:
            
                    print()
            
                    print(f"{sys.version_info}")
            
                    print()

                except Exception:

                    print()

                    print(page_divider_border_char * page_divider_border_num)

                    print()

                    print("Error #20 Printing Python Version Failed\n")

                    print(page_divider_border_char * page_divider_border_num)

                    print()

            elif terminal == "eval":

                try:

                    print()

                    print("[Eval Mode]")

                    print()

                    print("[Warning Eval Mode Evaluates Raw Python Expressions]")

                    print()

                    evalinput = input()

                    print()

                    print(eval(evalinput))

                    print()

                except Exception:

                    print()

                    print(page_divider_border_char * page_divider_border_num)

                    print()

                    print("Error #6 Eval Mode Failed\n")

                    print(page_divider_border_char * page_divider_border_num)

                    print()

            elif terminal == "len" or terminal == "length":

                try:

                    print()

                    print("[Len Mode]")

                    print()

                    len_directory = input(f"{dir_terminal_prompt_text}")

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

                except Exception:

                    print()

                    print(page_divider_border_char * page_divider_border_num)

                    print()

                    print("Error #7 Len Mode Failed\n")

                    print(page_divider_border_char * page_divider_border_num)

                    print()

            elif terminal == "infile" or terminal == "if":

                try:

                    print()

                    print("[Infile Mode]")

                    print()

                    Infile_mode_directory = input(f"{dir_terminal_prompt_text}")

                    print()

                    Infile_mode_stringtofind = input("Find:- ")

                    print()

                    with open(Infile_mode_directory, "r" , encoding = infile_mode_directory_encoding) as infile_mode_asfiledir:

                        if Infile_mode_stringtofind in infile_mode_asfiledir.read():

                            print(True)

                        else:

                            print(False)

                    print()

                except Exception:

                    print()

                    print(page_divider_border_char * page_divider_border_num)

                    print()

                    print("Error #8 Infile Mode Failed\n")

                    print(page_divider_border_char * page_divider_border_num)

                    print()

            elif terminal == "filesize" or terminal == "fs":

                try:

                    print()

                    print("[Filesize Mode]")

                    print()

                    filesize_mode_dir = input(f"{dir_terminal_prompt_text}")

                    print()

                    filesize_mode_size = os.path.getsize(filesize_mode_dir)

                    if filesize_mode_size == 1:

                        print(f"{filesize_mode_size} Byte")

                    else:

                        print(f"{filesize_mode_size} Bytes")

                    print()

                except Exception:

                    print()

                    print(page_divider_border_char * page_divider_border_num)

                    print()

                    print("Error #9 Filesize Mode Failed\n")

                    print(page_divider_border_char * page_divider_border_num)

                    print()

            elif terminal == "prt" or terminal == "print":

                try:

                    while True:

                        print_input = input()

                        if ":q" in print_input:

                            print()

                            break

                except Exception:
                    
                    print()

                    print(page_divider_border_char * page_divider_border_num)

                    print()

                    print("Error #10 Printing Failed\n")

                    print(page_divider_border_char * page_divider_border_num)

                    print()

            elif terminal == "replx" or terminal == "kw/r":

                try:
                    
                    print()

                    print("[Replx Mode]")

                    print()

                    replx_directory = input(f"{dir_terminal_prompt_text}")

                    print()

                    with open(replx_directory, "r", encoding = replx_mode_encoding_read) as replx_file:

                        contentreplxfile = replx_file.read()

                        search_keyword_replx_mode = input("Search:- ")

                        print()

                        replace_keyword_replx_mode = input("Replace:- ")

                        print()

                        replx_data = contentreplxfile.replace(search_keyword_replx_mode,replace_keyword_replx_mode)

                        with open(replx_directory, "w", encoding = replx_mode_encoding_write) as replx_file:

                            replx_file.write(replx_data)

                        print("Successfully replaced!")

                        print()

                except Exception:

                    print()

                    print(page_divider_border_char * page_divider_border_num)

                    print()

                    print("Error #11 Replx Mode Failed\n")

                    print(page_divider_border_char * page_divider_border_num)

                    print()

            elif terminal == "ls" or terminal == "lsdir":

                try:

                    print()

                    print("[List Mode]")

                    print()

                    ls_directory = input(f"{dir_terminal_prompt_text}")

                    print()

                    print(ls_dir_banner_divider_border_char * ls_dir_banner_divider_border_num)

                    print(f"Content of {ls_directory}:- ")

                    print(ls_dir_banner_divider_border_char * ls_dir_banner_divider_border_num)

                    listsdir = os.listdir(ls_directory)

                    for dircontentls in listsdir:

                        print()

                        print(dircontentls)

                    print()

                except Exception:

                    print()

                    print(page_divider_border_char * page_divider_border_num)

                    print()

                    print("Error #12 List Mode Failed\n")

                    print(page_divider_border_char * page_divider_border_num)

                    print()

            elif terminal == "mkdir" or terminal == "makedir":

                try:

                    print()

                    print("[Mkdir Mode]")

                    print()

                    mkdir_directory = pathlib.Path(input(f"{dir_terminal_prompt_text}")).expanduser()

                    mkdir_directory.mkdir(parents = True)

                    print()

                    print(f"{mkdir_successful_text}{mkdir_directory}")

                    print()

                except Exception:

                    print()

                    print(page_divider_border_char * page_divider_border_num)

                    print()

                    print("Error #13 Mkdir Mode Failed\n")

                    print(page_divider_border_char * page_divider_border_num)

                    print()

            elif terminal == "rmdir" or terminal == "removedir":

                try:

                    print()

                    print("[Rmdir Mode]")

                    print()

                    rmdir_directory = pathlib.Path(input(f"{dir_terminal_prompt_text}")).expanduser()

                    shutil.rmtree(rmdir_directory)

                    print()

                    print(f"{dir_successfully_deleted}")

                    print()

                except Exception:

                    print()

                    print(page_divider_border_char * page_divider_border_num)

                    print()

                    print("Error #14 Rmdir Mode Failed\n")

                    print(page_divider_border_char * page_divider_border_num)

                    print()

            elif terminal == "help" or terminal == "Help" or terminal == "?":

                try:

                    print()

                    print("[Help Mode]")

                    print()

                    print("""|List of all available valid commands|

1.) 0 or w or write | Write Mode [:s to save and quit and :q to quit without saving in Write Mode]

2.) 1 or q or quit | Quits the Editor

3.) 2 or r or read | Read Mode

4.) 3 or n or rename | Rename Mode

5.) 4 or d or delete | Delete Mode

6.) 5 or version | Prints Current Claw Version

7.) 6 or clr or clear or cls | Clears Screen with Banner

8.) 6. or clr. or clear. or cls. | Clears Screen without Banner

9.) 7 or a or append | Append Mode [:s to save and quit and :q to quit without saving in Append Mode]

10.) python | Prints Python Metadata

11.) pyver | Prints Python Version

12.) eval | Eval Mode

13.) len or length | Prints number of Characters in a File

14.) infile or if | Checks if a String Exists in a File or not

15.) filesize or fs | Prints File Size in Bytes

16.) prt or print | Prints in Terminal [Does not Write to a File]

17.) replx or kw/r | Replaces all Instances of a String with Another

18.) ls or lsdir | Lists all Items in a Directory

19.) mkdir or makedir | Creates New Directory [Folders]

20.) rmdir or removedir | Deletes a Directory and all Items Inside it

21.) help or Help or ? | Help Mode""")

                    print()

                except Exception:

                    print()

                    print(page_divider_border_char * page_divider_border_num)

                    print()

                    print("Error #21 Help Mode Failed\n")

                    print(page_divider_border_char * page_divider_border_num)

                    print()                

            else:

                print()

                print(page_divider_border_char * page_divider_border_num)

                print()

                print("Error #0 Unknown Command | Maybe Try \"help\" Command or \"?\" Command |\n")

                print(page_divider_border_char * page_divider_border_num)

                print()

except Exception:
                
    print()

    print(page_divider_border_char * page_divider_border_num)

    print()

    print("Error #22 Main Loop Failed\n")

    print(page_divider_border_char * page_divider_border_num)

    print()