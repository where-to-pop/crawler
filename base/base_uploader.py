class BaseUploader:
  def __init__(self, client):
    self.client = client
  
  def upload(self, data_list):
    raise NotImplementedError("upload 메서드는 서브클래스에서 구현해야 합니다.")