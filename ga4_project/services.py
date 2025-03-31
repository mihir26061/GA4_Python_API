import os
from django.conf import settings
from jj_data_connector.ga4 import GA4Report, Metrics, Dimensions
from datetime import datetime, timedelta

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = settings.GOOGLE_APPLICATION_CREDENTIALS
property_id = settings.PROPERTY_ID

ga4 = GA4Report(property_id)

def get_total_users():
    try:
        dimension_list = ['date', 'browser', 'googleAdsKeyword', 'engagementRate', 'averageSessionDuration']
        metric_list = ['totalUsers', 'bounceRate']
        date_range1 = ('2022-03-01', '2022-03-31')
        date_range2 = ('2022-04-01', '2022-04-30')

        # run the GA4 report
        report = ga4.run_report(
            dimension_list, 
            metric_list, 
            date_ranges=[date_range1, date_range2],
            row_limit=10,
            offset_row=0
        )
        return report
    except Exception as e:
        print("Error", e)
        return False

def get_month_start_end():
    today = datetime.today()
    start_of_month = today.replace(day=1)
    next_month = today.replace(day=28) + timedelta(days=4)  # Move to next month safely
    end_of_month = next_month.replace(day=1) - timedelta(days=1)
    return start_of_month.strftime('%Y-%m-%d'), end_of_month.strftime('%Y-%m-%d')
