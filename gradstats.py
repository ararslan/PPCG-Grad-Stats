import requests
import time
from datetime import datetime, timezone, timedelta


def get_questions(site, start, stop):
    """Get all questions from a site within a given date range.

    Args:
        site (string): Stack Exchange site to get questions from
        start (datetime): Beginning of date range for questions
        stop (datetime): End of date range for questions

    Returns:
        list: One dict per question

    Raises:
        ValueError: If the API response is an error

    """

    API_URL = "https://api.stackexchange.com/2.2/questions"

    api_parameters = {
        "site": site,
        "fromdate": int(start.timestamp()),
        "todate": int(stop.timestamp()),
        "pagesize": 100,
        "page": 1
    }

    questions = []

    while True:
        req = requests.get(API_URL, params=api_parameters)
        contents = req.json()

        if "error_id" in contents:
            raise ValueError(contents["description"])

        questions.extend(contents["items"])

        if not contents["has_more"]:
            break

        api_parameters["page"] += 1

        if "backoff" in contents:
            time.sleep(contents["backoff"])

    return questions


def get_area51_estimate(site):
    """Compute the average questions per day and answers per question.

    Args:
        site (string): Stack Exchange site to get questions from.

    Returns:
        (float, float): Questions per day, answers per question.

    Raises:
        Nothing, but may get a ValueError from get_questions.

    """

    now = datetime.now(timezone.utc)
    fortnight_ago = now - timedelta(days=14)
    questions = get_questions(site, fortnight_ago, now)

    avg_questions = len(questions) / 14

    if questions:
        avg_answers = sum(q["answer_count"] for q in questions) / len(questions)
    else:
        avg_answers = 0.0

    return avg_questions, avg_answers


if __name__ == "__main__":
    msg = """Over the past 2 weeks, PPCG has had...
{:.1f} questions per day
{:.1f} answers per question"""

    print(msg.format(*get_area51_estimate("codegolf")))

