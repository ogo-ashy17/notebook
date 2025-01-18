from azure.identity import DefaultAzureCredential
from azure.ai.ml import MLClient, command
from datetime import datetime

credential = DefaultAzureCredential()

ml_client = MLClient.from_config(credential=credential)

job = command(
    experiment_name='test-experiment',
    code='./',
    command='python training_script.py',
    environment='test-environment:1',
    compute='test-computing-cluster',
    display_name=f'run-{datetime.now().strftime("%Y%m%d%H%M%S")}'
)

ml_client.create_or_update(job)