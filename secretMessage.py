import os
def rename_files():
    list = os.listdir(r"E:\python programs\prank")
    print(list)
    saved_path = os.getcwd()
    #print("current_working Directory" +saved_path)
    os.chdir(r"E:\python programs\prank")
    print("current_working Directory" +saved_path)
    for file_name in list:
        #print("Old Name" + file_name)
        #print("New Name" + file_name.translate(str.maketrans('','','0123456789'))
        os.rename(file_name, file_name.translate(str.maketrans('','','0123456789')))
    os.chdir(saved_path)
rename_files()
