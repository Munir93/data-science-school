def move_blob(sourceLocation, destination):
    import os

    os.system('gsutil mv gs://' + sourceLocation + ' gs://' + destination + '')


move_blob('dod-mwja-project1/Completed/Source', 'dod-mwja-project1/Source')
