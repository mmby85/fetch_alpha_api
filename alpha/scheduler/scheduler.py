from apscheduler.schedulers.background import BackgroundScheduler
from alpha.views import DataViewset

def start():
  scheduler = BackgroundScheduler()
  data = DataViewset()
  scheduler.add_job(data.save_data_api, "interval", minutes=60,id="data_001",replace_existing=True)
  scheduler.start()