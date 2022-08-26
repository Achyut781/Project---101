import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        file = open(file_from, 'rb')
        dbx.files_upload(file.read(), file_to)

def main():
    access_token = 'sl.A9DZpgYRlwNDq7bFuJ85t-aihMAuHoyEHA3wKf2H5jMKnkNy9SCIIBB3x4jAeDIPjnPxhSBGyea84yjnz7SphUV4_zPe9MCfsgDQi1AMEqWKS1za96hIZCFqj-UcL419YYxhUMEsl.A9CXJQzaXiR_H3QbXVlTvQm8UF-92nwsqQFYElRgTtjR8yYnXBnwR9mUNAZJHF5AOJ5A43U72RL8Q4KPlJmTu1EpCd-9ceCU7ksAKBi2Mr6kGcpL9KZnPc3yyqwJyMtsroW1dcQ'
    transferdata = TransferData(access_token)
    file_from = input('Enter the file path to transfer')
    file_to = input('Enter the destination path for DropBox')
    transferdata.upload_files(file_from, file_to)
    print('Your desired file has been moved to DropBox. Thank You for using our program😊')

main()