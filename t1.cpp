#include <map>
#include <string>
#include <vector>
#include <list>
#include <algorithm>

class Solution
{
public:
    std::map<std::string, std::list<std::string>> graph;
    std::vector<std::string> ans;
    void dfs(std::string src)
    {

        while (!graph[src].empty())
        {
            std::string ngh = graph[src].front();
            graph[src].pop_front();
            dfs(ngh);
        }
        ans.push_back(src);
    }

    std::vector<std::string> findItinerary(std::vector<std::vector<std::string>> &edges)
    {
        for (int i = 0; i < edges.size(); ++i)
        {
            graph[edges[i][0]].push_back(edges[i][1]);
        }
        for (auto &ele : graph)
        {
            ele.second.sort();
        }

        dfs("JFK");
        reverse(ans.begin(), ans.end());
        return ans;
    }
};