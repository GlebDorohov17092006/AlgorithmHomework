#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#include <list>
using namespace std;

class StronglyConnected
{
private:
    int n;
    vector<list<int>> adj;
    vector<list<int>> rev;

    void dfs1(int u, vector<bool> &vis, stack<int> &st)
    {
        vis[u] = true;
        for (auto v : adj[u])
        {
            if (!vis[v])
            {
                dfs1(v, vis, st);
            }
        }
        st.push(u);
    }

    void dfs2(int u, vector<bool> &vis, vector<int> &comp, int id)
    {
        vis[u] = true;
        comp[u] = id;
        for (auto v : rev[u])
        {
            if (!vis[v])
            {
                dfs2(v, vis, comp, id);
            }
        }
    }

public:
    StronglyConnected(int size) : n(size)
    {
        adj.resize(n);
        rev.resize(n);
    }

    void addEdge(int u, int v)
    {
        adj[u].push_back(v);
        rev[v].push_back(u);
    }

    int minEdgesToStronglyConnected()
    {
        stack<int> st;
        vector<bool> vis(n, false);
        vector<int> comp(n, -1);

        for (int i = 0; i < n; i++)
        {
            if (!vis[i])
            {
                dfs1(i, vis, st);
            }
        }

        fill(vis.begin(), vis.end(), false);
        int compCount = 0;

        while (!st.empty())
        {
            int u = st.top();
            st.pop();

            if (!vis[u])
            {
                dfs2(u, vis, comp, compCount);
                compCount++;
            }
        }

        if (compCount == 1)
        {
            return 0;
        }

        vector<int> in(compCount, 0);
        vector<int> out(compCount, 0);

        for (int u = 0; u < n; u++)
        {
            for (int v : adj[u])
            {
                if (comp[u] != comp[v])
                {
                    out[comp[u]]++;
                    in[comp[v]]++;
                }
            }
        }

        int src = 0;
        int snk = 0;
        for (int i = 0; i < compCount; i++)
        {
            if (in[i] == 0)
                src++;
            if (out[i] == 0)
                snk++;
        }

        return max(src, snk);
    }
};