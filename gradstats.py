import requests, datetime, time

def seconds_since_epoch(dt):
    epoch = datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)
    return int((dt - epoch).total_seconds())

today = datetime.datetime.now(datetime.timezone.utc)

params = {
    "site": "codegolf",
    "fromdate": seconds_since_epoch(today - datetime.timedelta(days=14)),
    "todate": seconds_since_epoch(today),
    "page": 1
}

base_url = "https://api.stackexchange.com/2.2"

results = []

while True:
    req = requests.get(base_url + "/questions", params=params)
    contents = req.json()
    results.extend(contents["items"])
    if not contents["has_more"]:
        break
    if "backoff" in contents:
        time.sleep(contents["backoff"])
    params["page"] += 1

questions_per_day = len(results) / 14
answers_per_question = sum([q["answer_count"] for q in results]) / len(results)

print("Over the past 2 weeks, PPCG has had...")
print(round(questions_per_day, 1), "questions per day")
print(round(answers_per_question, 1), "answers per question")
