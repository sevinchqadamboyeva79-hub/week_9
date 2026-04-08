from dataclasses import dataclass,field
@dataclass
class CargoCrate:
    crate_id:str
    destination:str
    max_weight:float
    items:list[tuple[str,float]]=field(default_factory=list)
    def total_weight(self):
            return sum(weight for name,weight in self.items)
    def add_item(self, name: str, weight: float):
        if self.total_weight()+weight<=self.max_weight:
            self.items.append((name,weight))
            return True
        else:
            return False
    def manifest(self):
        print(f'Crate {self.crate_id} ->{self.destination}')
        for name,weight in self.items:
                print(f'  -{name}: {weight}kg')
        print(f'Total:{self.total_weight()}/{self.max_weight}kg')
c = CargoCrate("CR-401", "Arrakis", 50.0)
print(c.add_item("Stillsuit", 8.5))
print(c.add_item("Spice Melange", 30.0))
print(c.add_item("Shield Generator", 15.0))
print(c.total_weight())
c.manifest()
   


