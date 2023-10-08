from utils.app import *
from apscheduler.triggers.cron import CronTrigger

@app.route("/exporter", methods=["GET"])
def exporter():
    activity = json.loads(open("cleaned/activity.json").read())
    activity_by_app = json.loads(open("cleaned/activity_by_app.json").read())
    check_count = json.loads(open("cleaned/check_count.json").read())
    data = {
        "activity": activity,
        "activity_by_app": activity_by_app,
        "check_count": check_count,
    }
    return jsonify(data)


scheduler.add_job(
    importer,
    trigger=CronTrigger(hour=0, minute=0, second=0),
    id="midnight_job",
    replace_existing=True,
)

scheduler.start()

if __name__ == "__main__":
    app.run()
