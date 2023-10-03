# grasshopperSimulator

Grasshopper Simulator is a Python simulation made with pygame that emulates how grasshoppers with and without the ability to react to aggregation pheromones would live in a simulated environment.

First of all, we divided the area into a grid where each cell has three attributes: resources (green), humidity (blue), and temperature (red). The brighter the color, the more the conditions are favorable for the grasshoppers. The grasshoppers will consume a fixed quantity of resources from the cell they are in each turn, while the humidity and the temperature will randomly get more or less favorable. If a grasshopper can receive and produce the aggregating pheromone and the condition of the cell is adequate, it will do so and all the nearby grasshoppers that are receptive will move toward the cell. Otherwise, they will randomly move in the adjacent cells until they find one with good enough conditions. Every time a grasshopper moves it will have a certain probability of dying that is determined by the resources present in the cell and by the "predators" that will act more likely against smaller groups of grasshoppers. 

![Screenshot](/images/screenshot26.png "Screenshot")

The grid is shown four times, one for each resource, humidity, and temperature and one for the number of grasshoppers. The grasshopper's cells will acquire a whiter color when aggregation pheromones are active and in each cell are displayed on the left the aggregating grasshoppers and on the right the non-aggregating ones.
The program, based on the parameters in settings, will also generate a CSV file containing the number of grasshoppers and an images folder containing screenshots of the situation for every tick.
