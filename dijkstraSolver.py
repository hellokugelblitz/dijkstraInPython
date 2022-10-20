import vertex
import edge
import graph

def main():
    alphabet = ['a','b','c','d','e']

    a = vertex.Vertex(alphabet[0])
    b = vertex.Vertex(alphabet[1])
    c = vertex.Vertex(alphabet[2])
    d = vertex.Vertex(alphabet[3])

    a.addNeighbor(b, 5)
    b.addNeighbor(a,5)
    
    c.addNeighbor(b,2)
    




if __name__ == "__main__":
    main()