from bs4 import BeautifulSoup
import credentials
from playwright.sync_api import sync_playwright

login_payload = {"login": credentials.name,
                 "password": credentials.password}
grades = open("auto_grades.txt", "w")
names = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto(credentials.url)
    page.fill("input#UserName", login_payload["login"])
    page.fill("input#Password", login_payload["password"])
    page.locator('input:below(:text("Remember me?"))').click()
    html = page.inner_html('thead')
    page_soup = BeautifulSoup(html, "html.parser")
    task_names = page_soup.findAll("th", {"class": "text-center"})
    task_names = task_names[2:-1]
    for name in task_names:
        if '<a href="/Contests/' in str(name):
            name = (str(name).split(">"))[2]
        names.append(
            (str(name).replace('<th class="text-center">', "").replace("</th>", "").replace("/n", "").replace("</a", "")
             )[4:].strip())
    for i in range(1, credentials.max_pages + 1):
        page.goto(credentials.url_short + str(i))
        html = page.inner_html('tbody')
        page_soup = BeautifulSoup(html, "html.parser")
        students = page_soup.findAll("tr", {"class": ""})
        for student in students:
            all_info = student.findAll("td")
            grades.write(str(all_info[3:-1]).replace("<td>", "").replace("</td>", "") + "\n")

grades.close()
