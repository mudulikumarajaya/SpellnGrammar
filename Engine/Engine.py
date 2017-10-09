from gingerit.gingerit import GingerIt
import json

class Engine:

    def __init__(self):
        pass

    @classmethod
    def PredicationEngine(self, request):
        print("-----PredicationEngine------")
        ' Read the JSON  - Object'
        data = json.loads(request.body)
        input = {}

        'Get the Data Strings'
        input = data["InputData"]

        'Get the Object of the Ginger Objects'
        parser = GingerIt()

        'Get the Predictions'
        result = parser.parse(input + ' ')

        'Send the JSON results'
        return (result)
