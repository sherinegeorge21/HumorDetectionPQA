from locust import HttpUser, task, between

class CustomerSupportUser(HttpUser):
    wait_time = between(1, 5)  # Simulate realistic wait times between actions

    @task(10)
    def predict_normal_query(self):
        # Standard queries most likely to be sent to customer support
        self.client.post("/predict/", json={"text": "Where is my order?"})

    @task(3)
    def predict_humorous_query(self):
        # More humorous or playful interactions
        self.client.post("/predict/", json={"text": "Did my package go on a world tour?"})

    @task(1)
    def predict_complex_query(self):
        # Complex queries involving more detailed scenarios
        complex_text = "I ordered this item last year on a leap day, will it arrive only every four years?"
        self.client.post("/predict/", json={"text": complex_text})

    @task(5)
    def predict_mixed_emotions_query(self):
        # Queries that might contain mixed emotions or sarcasm
        mixed_text = "Great! My order is late again! What a surprise!"
        self.client.post("/predict/", json={"text": mixed_text})
