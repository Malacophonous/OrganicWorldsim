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
