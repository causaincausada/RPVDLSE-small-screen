class Result():
    def __init__(self, name="", date="", hour="", result=""):
        self.name = name
        self.date = date
        self.hour = hour
        self.result = result
    def crear_results():
        array_results = []
        for i in range(15):
            result = Result("img.jpg", "17/07/2022", "13:00", "ABC123")
            array_results.append(result)       
        return array_results



