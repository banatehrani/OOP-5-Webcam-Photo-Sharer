class FileSharer:

    def __init__(self, filepath, api_key="AviVqp7suSQWWEdrl6hf9z"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_fileLink = client.upload(filepath=self.filepath)
        return new_filelink.url
