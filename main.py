def main():
    print("Description:", end="\n\n")
    
    print(f"According to the Six Degrees of Kevin Bacon game, anyone in the Hollywood film industry can be connected to Kevin Bacon within six steps, where each step consists of finding a film that two actors both starred in.\n\nIn this problem, we are interested in finding the shortest path between any two actors by choosing a sequence of movies that connects them.\n\nFor example, the shortest path between Jennifer Lawrence and Tom Hanks is 2: Jennifer Lawrence is connected to Kevin Bacon by both starring in 'X-Men: First Class,' and Kevin Bacon is connected to Tom Hanks by both starring in 'Apollo 13.'\n\nWe can frame this as a search problem: our states are people. Our actions are movies, which take us from one actor to another (it is true that a movie could take us to multiple different actors, but that’s okay for this problem). Our initial state and goal state are defined by the two people we are trying to connect. By using breadth-first search, we can find the shortest path from one actor to another.")
    
    load_data()
    get_input()
    
def load_data():
  print("")
  
def get_input():
  print("Choose two actors.", end="\n\n")
  start_point = input("Name: ")
  end_point = input("Name: ")
  search(start_point, end_point)
  
def search(start_point, end_point):
  print("")
    
main()