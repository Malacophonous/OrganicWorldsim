ORGANIC WORLDSIM Readme
A project by Coniferous02

Goals of this project:
- A flexible open-world RPG in a simulated fantasy world where survival is not guaranteed
- Dynamic relationships between NPCS and NPCS and players
- Dynamic motivations for NPCS and Quests for players
- An deep dialogue and information sharing system
- A job and skill system that actually teach the player real-life knowledge
- The ability to convince opponents to quit fighting you (surrender/concede/walk away, etc)

Basically, these are some of the things I want the player to be able to do:
- Become the hero of a town, travel to a new town, and meet a number of fans
- Spread false rumors about the local constable being a coward in battle to replace him
- Make friends that inform you about the local lord's comings and goings
- Court the local lord's daughter, get married, and hire assassins to kill him
- Stumble upon a family travelling in the wilderness without adequate supplies or protection
- Cause a civil war by having your faction of friends support an upstart king
- Get accused of stealing or murder by a town that doesn't like you very much, even though you didn't do it
- Seek out clues and prove your innocence while on the run
- Get contracted as a spy for a big business and recover data on a rival's customers
- Court a commoner and get snubbed by your upper class friends
- Save a village from invasion by burning down their grain silo (only thing of value), get kicked out for it
- Help another npc find a home after being exiled, or join their quest to get un-exiled
- Cause fights at taverns all across the realm and watch the security presence get heavier
- Solve a crime by interviewing witnesses
- Take up performing, and get invited to the king's castle
- Start a business and hire npc help
- Buy, Bribe, and Blackmail favors      (Incentivize)
- Intimidate, Fight, or perform a feat of strength or combat to force a surrender    (Antagonize)
- Listen with an open ear and offer to help out other NPCS to make loyal friends    (Sympathize)

If that sounds awesome, Great! This game might be for you. You'll have to be patient though. I am only one guy.

Basic systems here:
NPC relationships are a directed graph, with an npc's attitude, respect and trust (ART) as edge attributes
NPCs have a memory of event records, each one a description of who did what, when, and how that changed the local world
NPCs have motivations based on Maslow's hierarchy of needs.
    -survival needs like food, clothing and shelter
    -safety needs like personal safety, financial safety, and a safety net
    -social needs like friends, intimacy, and love
    -esteem needs like self-esteem
    -life goals like being the best, seeking power or knowledge or hedonism or revenge
NPCs chose goals based on their needs and desires, then act on those goals, creating events
NPCs and the player can convey information to each other about events and people, altering their relationships with the updated info
NPCs have daily routines as determined by their job


# OrganicWorldsim
Python 3 based package for simulating NPC motivations and relationships in an open-world RPG


You will need: Python 3.4 or later, nx (the graph networking library for python), patience

The main() function is contained in the gamelogic.py file.

The game world simulates time and location currently. Will eventually feature weather and structures.

The npcs have a motivation system based on Maslow's hierarchy of needs (Survival, safety, belonging, esteem, and self-actualization)

The npcs have goals within a tree structure (to be implemented) that lead to actions

Actions are evaluated taking into account not only Maslow's but also other npcs' reactions to that action

Relationships are measured and evaluated on a basis of Attitude, respect, and trust, or ART

NPCs have routines, memories of events, and can share information about them.

