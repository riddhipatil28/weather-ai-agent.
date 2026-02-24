class Planner:

    def create_plan(self, user_message):

        msg = user_message.lower()

        if "predict" in msg or "tomorrow" in msg:
            return ["detect_city", "get_weather", "predict_temp"]

        return ["detect_city", "get_weather"]
