import jupyter_to_medium as jtm
import os

jtm.publish('2021/june/2_multiclass_metrics/multiclass_metrics.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title='Comprehensive Guide on Multiclass Classification Metrics',
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
