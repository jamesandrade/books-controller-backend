from src.modules.Reports.services.topFiveService import topFiveService

def topFive(start_date, end_date):
    return topFiveService.execute(start_date, end_date)
