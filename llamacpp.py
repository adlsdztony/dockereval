import os
from dotenv import load_dotenv

from openai import OpenAI
from httpx import Timeout

from mix_eval.models.base_api import APIModelBase
from mix_eval.api.registry import register_model

@register_model("llamacpp") ## 修改模型注册名
class LLAMACPP(APIModelBase): ## 修改class名
    def __init__(self, args):
        super().__init__(args)
        self.args = args
        self.model_name = 'llamacpp' ## 修改成模型注册名

        load_dotenv()
        self.client = OpenAI(
            api_key="llamacpp", ## 添加api_key，可填写为任意非none字符串
            base_url="http://llamacpp:8000/v1", ## 添加base_url为localhost
            timeout=Timeout(timeout=100.0, connect=20.0)
        )