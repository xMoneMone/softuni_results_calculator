name = input("Input username: ")
password = input("Input password: ")
url = input("Input url of the first page of the results: ")
if "page=1" not in url:
    url += "?page=1"
url_short = url[:-1]
max_pages = int(input("Input the number of result pages (number of last page): "))
task_per_person = int(input("Input number of tasks received per person: "))