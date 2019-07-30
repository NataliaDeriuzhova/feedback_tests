import pytest
import requests
from hamcrest import assert_that, equal_to

URL = "http://localhost:58001/nps"
STATUS_OK = 200
STATUS_ERROR = 400


class TestFeedbackPositive:
    test_data_with_feedback = [
        ("0", "Autotest feedback with 0 mark"),
        ("1", "Autotest feedback with 1 mark"),
        ("2", "Autotest feedback with 2 mark"),
        ("3", "Autotest feedback with 3 mark"),
        ("4", "Autotest feedback with 4 mark"),
        ("5", "Autotest feedback with 5 mark"),
        ("6", "Autotest feedback with 6 mark"),
        ("7", "Autotest feedback with 7 mark"),
        ("8", "Autotest feedback with 8 mark"),
        ("9", "Autotest feedback with 9 mark"),
        ("10", "Autotest feedback with 10 mark")
    ]

    @pytest.mark.parametrize("user_action, feedback", test_data_with_feedback)
    def test_mark_with_feedback_positive(self, user_action, feedback):
        data = ({"user_action": user_action, "feedback": feedback})
        response = requests.post(URL, json=data)
        assert_that(response.status_code, equal_to(STATUS_OK), "Запрос вернул status=ok для оценок 0-10 с комментарием")

    test_data_without_feedback = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10"
    ]

    @pytest.mark.parametrize("user_action", test_data_without_feedback)
    def test_mark_without_feedback_positive(self, user_action):
        data = ({"user_action": user_action})
        response = requests.post(URL, json=data)
        assert_that(response.status_code, equal_to(STATUS_OK),
                    "Запрос вернул status=ok для оценок 0-10 без комментария")

    test_data = [
        ("abracadabra", ""),
        ("", ""),
        ("11", ""),
        ("-1", "")
    ]
 
    @pytest.mark.parametrize("user_action, feedback", test_data)
    def test_send_feedback_negative(self, user_action, feedback):
        data = ({"user_action": user_action, "feedback": feedback})
        response = requests.post(URL, json=data)
        assert_that(response.status_code, equal_to(STATUS_ERROR), "Запрос вернул status=error")
