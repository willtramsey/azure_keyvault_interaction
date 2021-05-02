# source: https://docs.microsoft.com/en-us/azure/key-vault/secrets/quick-create-python#grant-access-to-your-key-vault

# This file can be used to connect to Azure (using az login) to send new secrets to Azure Key Vault
# (or retrieve existing secrets)

import os
import cmd
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential,AzureCliCredential

keyVaultName = 'metro-snow-keyvault'
KVUri = "https://metro-snow-keyvault.vault.azure.net"

credential = AzureCliCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

secretName = "wramsey"
secretValue = "P0#erBI"


# client.set_secret(secretName, secretValue)
retrieved_secret = client.get_secret(secretName)
print(retrieved_secret.value)





# print(f"Your secret is '{retrieved_secret.value}'.")
# print(f"Deleting your secret from {keyVaultName} ...")

# poller = client.begin_delete_secret(secretName)
# deleted_secret = poller.result()

# print(" done.")