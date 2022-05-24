from dataclasses import dataclass

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import config


@dataclass
class DesireSessionDetails:
    day_to_book: str
    day_of_session: str
    time_wanted_12h: str
    time_wanted_24h: str


sesh1 = DesireSessionDetails(day_to_book="friday",
                             day_of_session="monday",
                             time_wanted_12h="6:00 am",
                             time_wanted_24h="06:00")

sesh2 = DesireSessionDetails(day_to_book="saturday",
                             day_of_session="tuesday",
                             time_wanted_12h="6:00 am",
                             time_wanted_24h="06:00")

sesh3 = DesireSessionDetails(day_to_book="sunday",
                             day_of_session="wednesday",
                             time_wanted_12h="6:00 am",
                             time_wanted_24h="06:00")

sesh4 = DesireSessionDetails(day_to_book="tuesday",
                             day_of_session="friday",
                             time_wanted_12h="6:00 am",
                             time_wanted_24h="06:00")
sesh5 = DesireSessionDetails(day_to_book="wednesday",
                             day_of_session="saturday",
                             time_wanted_12h="10:30 am",
                             time_wanted_24h="10:30")

mohannad_classes = [sesh1, sesh2, sesh3, sesh4, sesh5]


def register_for_class():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://app.wodify.com/SignIn/Login?OriginalURL=&RequiresConfirm=false")
    time.sleep(2)

    id_box = driver.find_element(By.ID, 'Input_UserName')
    id_box.send_keys(config.username)

    password_box = driver.find_element(By.ID, 'Input_Password')
    password_box.send_keys(config.password)

    button = driver.find_element(By.CSS_SELECTOR, '[data-button]')
    button.click()
    time.sleep(2)

    driver.get("https://app.wodify.com/Schedule/CalendarListViewEntry.aspx")
    time.sleep(3)

    table = driver.find_element(By.ID, 'AthleteTheme_wt6_block_wtMainContent_wt9_wtClassTable')
    table_body = table.find_element(By.TAG_NAME, 'tbody')
    days_and_classes = table_body.find_elements(By.CSS_SELECTOR, "tr[style]")

    days_of_week = table_body.find_elements(By.CSS_SELECTOR, "tr[style='']")

    sesh = get_day_row(days_and_classes, days_of_week)

    register_button = sesh.find_element(By.CLASS_NAME, "svgContainer")
    register_button.click()

    input()


def get_day_row(sess_list, day_list):
    day_of_week_list = day_list
    session_list = sess_list

    wanted_day = "thursday"
    wanted_time_12h = "4:00 pm"
    wanted_time_24h = "16:00"

    for day_of_week in day_of_week_list:
        print(day_of_week.text)
        if wanted_day in day_of_week.text.lower():
            wanted_day_index = session_list.index(day_of_week) + 1
            index_of_next_day = day_of_week_list.index(day_of_week) + 1

            if index_of_next_day > len(day_of_week_list) - 1:
                next_day_index = len(session_list)
            else:
                next_day = day_of_week_list[index_of_next_day]
                next_day_index = session_list.index(next_day)

            for i in range(wanted_day_index, next_day_index):
                session = session_list[i]
                print(session.text)
                if "pm\n" in session.text.lower() or "am\n" in session.text.lower():
                    if wanted_time_12h in session.text.lower():
                        print("the 12h session we want is " + session.text + " on " + wanted_day)
                        return session
                else:
                    if wanted_time_24h in session.text.lower():
                        print("the 24h session we want is " + session.text + " on " + wanted_day)
                        return session
            print("Could not find class for time " + wanted_time_12h + " 12H or " + wanted_time_24h + " 24H on " +
                  wanted_day)
            return
    print("could not find day of week " + wanted_day)


if __name__ == '__main__':
    register_for_class()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

    # session_list = [
    #     "THURSDAY\n19/05/2022",
    #     "CrossFit 6:00 AM",
    #     "CrossFit 7:00 AM",
    #     "CrossFit 08:00",
    #     "CrossFit 9:30 AM",
    #     "CrossFit 12:00",
    #     "Open Gym 16:00",
    #     "CrossFit 5:15 PM",
    #     "CrossFit 6:15 PM",
    #     "CrossFit 7:15 PM",
    #     "FRIDAY\n20/05/2022",
    #     "CrossFit 6:00 AM",
    #     "CrossFit 7:00 AM",
    #     "CrossFit 08:00",
    #     "CrossFit 9:30 AM",
    #     "CrossFit 12:00",
    #     "Open Gym 16:00",
    #     "CrossFit 5:15 PM",
    #     "CrossFit 6:15 PM",
    #     "CrossFit 7:15 PM",
    #     "SATURDAY\n21/05/2022",
    #     "Barbell 08:00",
    #     "Barbell 09:15",
    #     "CrossFit 10:30",
    #     "SUNDAY\n22/05/2022",
    #     "Open Gym 08:00",
    #     "Gas Tank 09:00",
    #     "Gas Tank 09:45",
    #     "Gas Tank 10:30",
    #     "MONDAY\n23/05/2022",
    #     "CrossFit 6:00 AM",
    #     "CrossFit 7:00 AM",
    #     "CrossFit 08:00",
    #     "CrossFit 9:30 AM",
    #     "CrossFit 12:00",
    #     "Open Gym 16:00",
    #     "CrossFit 5:15 PM",
    #     "CrossFit 6:15 PM",
    #     "CrossFit 7:15 PM",
    #     "TUESDAY\n24/05/2022",
    #     "CrossFit 6:00 AM",
    #     "CrossFit 7:00 AM",
    #     "CrossFit 08:00",
    #     "CrossFit 9:30 AM",
    #     "CrossFit 12:00",
    #     "Open Gym 16:00",
    #     "CrossFit 5:15 PM",
    #     "CrossFit 6:15 PM",
    #     "CrossFit 7:15 PM",
    # ]
    #
    # day_of_week_list = [
    #     "THURSDAY\n19/05/2022",
    #     "FRIDAY\n20/05/2022",
    #     "SATURDAY\n21/05/2022",
    #     "SUNDAY\n22/05/2022",
    #     "MONDAY\n23/05/2022",
    #     "TUESDAY\n24/05/2022",
    # ]
