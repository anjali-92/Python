def create_task_list():
    print "\nEnter tasks type done when completed entering tasks."
    task_list = []
    task_counter = 1
    while(1):
        task = raw_input("\n")
        if task != 'done':
            task = str(task_counter) + "  " +task
            task_list.append(task)
            task_counter = task_counter + 1
        else:
            break
    return task_list

def save_task_list(task_list):
    from time import strftime
    date_fmt = strftime("%d-%m-%Y %H:%M:%S")
    print task_list

    file_date = strftime("%d-%m-%Y")
    with open(file_date, "a+") as f:
        f.write(date_fmt)
        f.writelines("\n    %s "% task for task in task_list)
        f.write("\n\n")
        #f.write("\n".join(task_list))

if __name__ == '__main__':
    task_list = create_task_list()
    save_task_list(task_list)
