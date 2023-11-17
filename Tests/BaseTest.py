import datetime
from random import randint
import pytest


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class BaseTest:

    def generate_email_with_timestamp(self):
        time_stamp = datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S")
        return "testaccount" + time_stamp + "@gmail.com"

    def generate_telephone_number_with_random(self):
        num = ''.join(str(randint(0, 10)) for _ in range(9))
        return "9" + num

    def generate_screenshots(self, name):
        self.driver.get_screenshot_as_file(".\\Screenshots\\"+name+".png")
