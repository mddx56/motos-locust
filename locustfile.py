from locust import HttpUser, task


headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjQiLCJ1c2VybmFtZSI6InZpYW4xIiwicmVhbG5hbWUiOiJIb25kYSBWaWFuICIsInN0YXR1cyI6MSwicm9sZSI6MSwiaWF0IjoxNzAxMTU0ODQzLCJleHAiOjE3MDE3NTk2NDN9.5JnLryJjIGUCIveNwf1LKL1s965qlruhwjOAz49DNCE",
    "Content-Type": "application/json",
}


class MotosApi(HttpUser):
    @task
    def positions_test(self):
        self.client.get("/")
        self.client.get("/api/position", headers=headers)
