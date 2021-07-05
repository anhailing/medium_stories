import jupyter_to_medium as jtm
import os

jtm.publish('2021/july/2_matplotlib_vs_plotly/matplotlib_vs_plotly.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title='',
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
