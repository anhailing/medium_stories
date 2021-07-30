import jupyter_to_medium as jtm
import os

jtm.publish('2021/july/9_optuna/tune_optuna2.ipynb',
            integration_token=os.environ['TOKEN'],
            pub_name=None,
            title='Why Is Everyone at Kaggle Obsessed with Optuna For Hyperparameter Tuning?',
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )
