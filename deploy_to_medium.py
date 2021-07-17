import jupyter_to_medium as jtm
import os

jtm.publish('2021/july/6_stationarity_ts/stationarity.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title='How to Remove Non-Stationarity in Time Series Forecasting',
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
