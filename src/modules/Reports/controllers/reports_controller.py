from src.modules.Reports.services.topFiveService import topFiveService
from src.modules.Reports.services.topAllService import topAllService

def topFive(start_date, end_date):
    return topFiveService.execute(start_date, end_date)
def topAll(start_date, end_date):
    return topAllService.execute(start_date, end_date)
