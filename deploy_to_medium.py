import jupyter_to_medium as jtm

jtm.publish('merge_data_article/main.ipynb',
            integration_token="",
            pub_name=None,
            title=None,
            tags=None,
            publish_status='draft',
            notify_followers=False,
            license='all-rights-reserved',
            canonical_url=None,
            chrome_path=None,
            save_markdown=False,
            table_conversion='chrome'
            )