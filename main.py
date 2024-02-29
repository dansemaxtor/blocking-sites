from datetime import datetime as dt


# forwarding address
redirect = "127.0.0.1"
# a file for recording all changes
host_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
# list of sites
site_list = []
# setting the time
now = dt.now()
my_time_1 = now.replace(hour=8, minute=0, second=0, microsecond=0)
my_time_2 = now.replace(hour=10, minute=0, second=0, microsecond=0)

#Open the file, if the file is empty, then we ask the user 
#for input, and transfer it to the list of sites, if it is 
#not empty, then we lock the data from the file and transfer 
#it to the list of sites
def write_list():
    try:
        with open("text.txt", 'r+') as file:
            content = file.read()
            if content == '':
                list_input = input("Введите название сайтов через запятую: ").split(",")
                file.write(",".join(list_input))
                for list in list_input:
                    site_list.append(list)
            else:
                for list in content.split(","):
                    site_list.append(list)
    except:
        print("Внимание ошибка!!!")


#We run the program, if the time interval 
#that we need writes the list to the "hosts" 
#file, if the interval that we do not need is 
#deleted, these addresses are deleted
while True:
    write_list()

    if my_time_1 < now < my_time_2:
        with open(host_path, "r+") as file:
            content = file.read()
            for website in site_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in site_list):
                    file.write(line)
                file.truncate()
