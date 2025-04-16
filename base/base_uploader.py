from database import ElasticsearchClient

class BaseUploader:
  def __init__(self):
    self.client = ElasticsearchClient.get_client()
  
  def upload(self, data_list):
    raise NotImplementedError("upload 메서드는 서브클래스에서 구현해야 합니다.")