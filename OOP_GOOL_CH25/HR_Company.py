class Worker():
    def __init__(self, id, name, experience):
        self.id = id
        self.name = name
        self.experience = experience

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, experience: {self.experience}"

    def get_salary(self):
        return self.experience * 1000


w = Worker('123456781', 'israel Mor', 6)
print(w)
print(w.get_salary())


class Manager(Worker):
    def __init__(self, id, name, experience, managed_workers_num):
        super().__init__(id, name, experience)
        self.managed_workers_num = managed_workers_num

    def __repr__(self):
        s = Worker.__repr__(self) + f", workers: {self.managed_workers_num}"
        return s

    def get_salary(self):
        salary = Worker.get_salary(self) + (self.managed_workers_num * 200)
        return salary

m = Manager('123456784', 'israel Dan', 20, 2)
print(m)
print(m.get_salary())


class Company():
    def __init__(self, name, workers):
        self.name = name
        workers_id = []
        for worker in workers:
            workers_id.append(worker.id)
        for each_workers_id in workers_id:
            if (workers_id.count(each_workers_id) > 1):
                raise ValueError("Identical Id's are NOT valid")
        self.workers = workers

    def __repr__(self):
        s = "Company:" + self.name + "\n"
        for worker in self.workers:
            s += worker.__repr__() + "\n"
        return s[:-1]

    def check_managers(self, threshold):
        is_threshold = []
        for worker in self.workers:
            if isinstance(worker, Manager):
                if worker.managed_workers_num >= threshold:
                    is_threshold.append(True)
                else:
                    is_threshold.append(False)

        if False in is_threshold:
            return False
        return True


    def get_highest_earning_worker(self):
        return max(self.workers, key=lambda x:x.get_salary())


w1 = Worker('123456781', 'israel Mor', 6)
w2 = Worker('123456782', 'israel Shahar', 9)
w3 = Worker('123456783', 'israel Shalom', 4)
m1 = Manager('123456784', 'israel Dana', 20, 2)
m2 = Manager('123456785', 'israel Moshe', 30, 1)


c = Company("WIX", [w1, w2, w3, m1, m2])
print(c)
print(c.check_managers(2))

print(c.get_highest_earning_worker())
