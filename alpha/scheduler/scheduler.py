from app.settings import TIME_ZONE
from apscheduler.schedulers.background import BackgroundScheduler
from alpha.views import DataViewset

def start():
  scheduler = BackgroundScheduler({'apscheduler.timezone': TIME_ZONE})
  data = DataViewset()
  scheduler.add_job(data.save_data_api, "interval", minutes=1,id="data_001",replace_existing=True)
  scheduler.start()