
from gameworld.world import World
from gameworld.entities.npcs.npc import NPC
from gameworld.interactables.items.item import Item


def main():
    W = World()
    for name in ['Jim', 'Frank', 'Susan', 'Betty']:
        W.addNPC(NPC(name))
    W.addRelationship('Jim','Frank')    #tests name lookups and default data
    W.addRelationship('Jim','Susan',(100,100,100),'wife')      #tests art and label assignment
    W.addRelationship('Susan','Jim',(100,100,100),'husband')    #tests bilateral edge
    W.addRelationship(W.npcs[0],W.npcs[3])    #tests node number lookup, should be jim knows betty
    W.addRelationship(W.npcnames['Betty'],W.npcnames['Susan'])

    for item, x, y in zip(['cup', 'sword', 'coin'], [0, 0, 5], [0, 1, 5]):
        W.items[(x,y)] = Item(item,x,y)
    foo = [(0,0),(5,5),(4,4),(10,1)]
    for coord,npc in zip(foo,W.npcs.values()):
        npc.x = coord[0]
        npc.y = coord[1]
    for npc in W.npcs.values():
        npc.PrintStatus(W.SG)
        for item in npc.PercieveAreaItems(W):
            item.PrintStatus()
        for other in npc.PercieveAreaPeople(W):
            print(other.name)

if __name__ == '__main__':
    main()
