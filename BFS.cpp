#include <iostream>
#include <queue>
#include <vector>

using namespace std;

void bfs(vector<vector<int>>& graph, int start) {
    int numNodes = graph.size();
    vector<bool> visited(numNodes, false); // Array to store visited nodes
    queue<int> q;                          // Queue for BFS

    visited[start] = true;                 // Mark the start node as visited
    q.push(start);                         // Enqueue the start node

    while (!q.empty()) {
        int node = q.front();               // Dequeue a node from the front of the queue
        q.pop();
        cout << node << " ";                // Process the node (e.g., print it)

        // Explore all the neighboring nodes of the current node
        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {       // If neighbor is not visited
                visited[neighbor] = true;   // Mark it as visited
                q.push(neighbor);           // Enqueue the neighbor node
            }
        }
    }
}

int main() {
    int numNodes = 7;  // Number of nodes in the graph

    // Create an adjacency list representation of the graph
    vector<vector<int>> graph(numNodes);

    // Add edges
    graph[0] = {1, 2};
    graph[1] = {0, 3, 4};
    graph[2] = {0, 5, 6};
    graph[3] = {1};
    graph[4] = {1};
    graph[5] = {2};
    graph[6] = {2};

    int startNode = 0; // Starting node for BFS
    bfs(graph, startNode);

    return 0;
}

