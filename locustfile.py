# An example on how to nest tasksets

from locust import HttpLocust, TaskSet, TaskSequence, task, seq_task, between

class ForumPage(TaskSequence):
    # wait_time can be overridden for individual TaskSets
    #wait_time = between(1, 2)

    @seq_task(1)
    def index(self):
        self.client.get("/search?q=resilience")
        print('tarea 1-1-request 1')
        self.client.get("/search?q=sapience")
        print('tarea 1-1-request 2')

    @seq_task(2)    
    def other(self):
        self.client.get("/search?q=google")
        print('tarea 1-2')
        self.interrupt()

class AboutPage(TaskSet):
    @task(10)
    def index(self):
        self.client.get("/")
        print('tarea 2-1')
        
    @task(10)
    def index2(self):
        self.client.get("/search?q=locust")
        print('tarea 2-2')

    @task(15)
    def index3(self):
        self.client.get("/search?q=jmeter")
        print('tarea 2-3')
        self.interrupt()
    

class WebsiteTasks(TaskSet):
    # We specify sub TaskSets using the tasks dict
    tasks = {
        ForumPage: 400,
        AboutPage: 10,
    }
    
    @task(10)
    def index(self):
        self.client.get("/search?q=games+week")
        print('tarea 3')

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(0, 5)