import jupyter_to_medium as jtm
import os

jtm.publish('2023/2_february/1_outlier_detection_102/notebook.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title="How to Easily Perform Outlier Detection In Python For Machine Learning, #2",
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
