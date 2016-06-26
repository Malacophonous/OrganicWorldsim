
from gameworld.world import World
from gameworld.entities.npcs.npc import NPC
from gameworld.interactables.items.item import Item
from gameworld.entities.peoplemanager import PeopleManager


def main():
    W = World()
    PM = PeopleManager(W)
    PM.loadNPCConfig()
    PM.populateWorld()


    for item, x, y in zip(['cup', 'sword', 'coin'], [0, 0, 5], [0, 1, 5]):
        W.items[(x,y)] = Item(item,x,y)
    foo = [(0,0),(5,5),(4,4)]
    for coord,npc in zip(foo,PM.npcs.values()):
        npc.x = coord[0]
        npc.y = coord[1]
    for npc in PM.npcs.values():
        npc.PrintStatus(PM.SG)
        for item in npc.PercieveAreaItems(W):
            item.PrintStatus()
        for other in npc.PercieveAreaPeople(W):
            print(other.name)

if __name__ == '__main__':
    main()
