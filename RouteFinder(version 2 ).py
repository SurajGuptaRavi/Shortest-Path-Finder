class RouteFinder:
    def __init__(self,routes):
        self.routes = routes
        self.routes_dict = {}


        for start , end in self.routes:
            if start not in self.routes_dict:
                self.routes_dict[start] = []

            if end not in self.routes_dict:
                self.routes_dict[end] = []

            self.routes_dict[start].append(end)
            self.routes_dict[end].append(start)




        print(f"forward_dict = {self.routes_dict}")


    def get_all_path(self,start,end,path=[]):
        path = path + [start]
        if start is end:
            return [path]
        if start not in self.routes_dict:
            return []
        paths = []
        for each_stop in self.routes_dict[start]:
            if each_stop not in path:
                new_path = self.get_all_path(each_stop,end,path)

                for each_path in new_path:
                    paths.append(each_path)

        return paths

    def get_shortest_path(self,start,end,path=[]):
        path = path + [start]
        if start is end:
            return path
        if start not in self.routes_dict:
            return None

        sp = None
        for each_stop in self.routes_dict[start]:
            if each_stop not in path:
                new_path = self.get_shortest_path(each_stop,end,path)

                if new_path is not None:
                    if sp is None or len(new_path) < len(sp):
                        sp = new_path

        return sp

routes = [
    ('virar','dahanu road'),
    ('virar','nalasopara'),
    ('nalasopara','vasai'),
    ('vasai','naigaon'),
    ('vasai','juchandra'),
    ('juchandra','kaman'),
    ('kaman','kharbao'),
    ('kharbao','bhiwandi'),
    ('bhiwandi','kopar'),
    ('naigaon','bhayandar'),
    ('bhayandar','mira road'),
    ('mira road','dahisar'),
    ('dahisar','borivali'),
    ('borivali','andheri'),
    ('andheri','bandra'),
    ('bandra','dadar'),
    ('dadar','byculla'),
    ('dadar','kurla'),
    ('dadar','mumbai central'),
    ('mumbai central','marine lines'),
    ('marine lines','churchgate'),
    ('byculla','cst'),
    ('kurla','ghatkopar'),
    ('ghatkopar','thane'),
    ('thane','kopar'),
    ('kopar','kalyan'),
    ('kalyan','titwala'),


]

start = "titwala"
end = "cst"

rf = RouteFinder(routes)
result = rf.get_all_path(start,end)
print(f"Path between {start} and {end} ")

for e in result:
    print(e)
else:
    print(f"\n\nShortest route between {start} and {end} is :-")
    print(rf.get_shortest_path(start,end))
