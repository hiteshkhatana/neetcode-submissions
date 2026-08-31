import base64, json
class Solution:

    def encode(self, strs: List[str]) -> str:
        strs_input = json.dumps(strs)
        print(strs_input,"--inc")
        return base64.b64encode(strs_input.encode()).decode()

    def decode(self, s: str) -> List[str]:
        strs = base64.b64decode(s).decode()
        print(strs)
        return json.loads(strs)