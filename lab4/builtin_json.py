import json
def use_json():
    data = {"status": "success", "code": 200}
    print(f"json: {json.dumps(data)}")