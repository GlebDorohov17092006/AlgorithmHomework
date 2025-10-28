#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

class ShortestPaths
{
private:
    int n;
    vector<vector<int>> adj;

public:
    ShortestPaths(int size) : n(size)
    {
        adj.resize(n);
    }

    void addEdge(int u, int v)
    {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int countShortestPaths(int start, int end)
    {
        vector<int> dist(n, INT_MAX);
        vector<int> cnt(n, 0);
        vector<bool> vis(n, false);

        dist[start] = 0;
        cnt[start] = 1;

        queue<int> q;
        q.push(start);
        vis[start] = true;

        while (!q.empty())
        {
            int u = q.front();
            q.pop();

            for (int v : adj[u])
            {
                if (!vis[v])
                {
                    vis[v] = true;
                    dist[v] = dist[u] + 1;
                    cnt[v] = cnt[u];
                    q.push(v);
                }
                else if (dist[v] == dist[u] + 1)
                {
                    cnt[v] += cnt[u];
                }
            }
        }

        return cnt[end];
    }
};