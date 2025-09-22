#include <iostream>
#include <vector>
#include <stdexcept>
#include <memory>
#include <algorithm>

using namespace std;


enum COLOR
{
    WHITE = 0,
    GRAY = 1,
    BLACK = 2
};

class Graph
{
private:
    vector<vector<int>> graph;

    void dfs(int v, int &timer, vector<COLOR> &color, vector<int> &parent, 
             vector<int> &t_in, vector<int> &t_out, vector<int> &ans)
    {
        color[v] = GRAY;
        t_in[v] = timer++;
        
        for(int ch : graph[v])
        {
            if(color[ch] == WHITE)
            {
                parent[ch] = v;
                this->dfs(ch, timer, color, parent, t_in, t_out, ans);
            }
        }

        t_out[v] = timer++;
        ans.push_back(v);
        color[v] = BLACK;
    }

    bool dfs_cycle(int v, vector<COLOR> &color)
    {
        color[v] = GRAY;
        
        for(int ch : graph[v])
        {
            if(color[ch] == WHITE)
            {
                if(dfs_cycle(ch, color))
                    return true;
            }
            else if(color[ch] == GRAY)
            {
                return true;
            }
        }

        color[v] = BLACK;
        return false;
    }

    bool has_cycle()
    {
        vector<COLOR> color(graph.size(), WHITE);
        for(int i = 0; i < graph.size(); ++i)
        {
            if (color[i] == WHITE)
            {
                if (dfs_cycle(i, color))
                {
                    return true;
                }
            }
        }
        return false;
    }

public:
    Graph(vector<vector<int>> gr) : graph(gr) {}

    vector<int> topological_sort()
    {
        if (this->has_cycle())
        {
            throw runtime_error("Graph contains cycles!");
        }
        
        vector<COLOR> color(graph.size(), WHITE); 
        vector<int> parent(graph.size(), -1);
        vector<int> t_in(graph.size(), -1);
        vector<int> t_out(graph.size(), -1);
        vector<int> ans;
        int timer = 0;

        for(int i = 0; i < graph.size(); ++i)
        {
            if(color[i] == WHITE)
            {
                this->dfs(i, timer, color, parent, t_in, t_out, ans);
            }
        }

        reverse(ans.begin(), ans.end());
        return ans;
    }
};


class Vertex 
{
public:
    virtual ~Vertex() = default;
    virtual int num_inputs() const = 0;
    virtual void set_input(int inp_idx, double inp_val) = 0;
    virtual int num_outputs() const = 0;
    virtual double get_output(int out_idx) = 0;
    virtual void calc_value() = 0;
};

struct Edge {
    int out_vertex_id;
    int out_port_id;
    int inp_vertex_id;
    int inp_port_id;
};

class PlusOperator : public Vertex 
{
    double m_inp_val[2] = {0};
    double m_out_val = 0;
public:
    int num_inputs() const override 
    { 
        return 2; 
    }
    
    void set_input(int inp_idx, double inp_val) override 
    {
        if(inp_idx < 0 || inp_idx >= 2)
            throw out_of_range("Bad inp_idx in PlusOperator::set_input");
        m_inp_val[inp_idx] = inp_val;
    }
    
    void calc_value() override 
    {
        m_out_val = m_inp_val[0] + m_inp_val[1];
    }
    
    int num_outputs() const override 
    {
        return 1; 
    }
    
    double get_output(int out_idx) override 
    {
        if(out_idx != 0) throw out_of_range("Bad out_idx");
        return m_out_val;
    }
};

class MultiplyOperator : public Vertex 
{
    double m_inp_val[2] = {0};
    double m_out_val = 0;
public:
    int num_inputs() const override 
    { 
        return 2; 
    }
    
    void set_input(int inp_idx, double inp_val) override 
    {
        if(inp_idx < 0 || inp_idx >= 2)
            throw out_of_range("Bad inp_idx in MultiplyOperator::set_input");
        m_inp_val[inp_idx] = inp_val;
    }
    
    void calc_value() override 
    {
        m_out_val = m_inp_val[0] * m_inp_val[1];
    }
    
    int num_outputs() const override { return 1; }
    
    double get_output(int out_idx) override {
        if(out_idx != 0) throw out_of_range("Bad out_idx");
        return m_out_val;
    }
};

class CalcGraph : public Vertex {
private:
    vector<unique_ptr<Vertex>> vertices;
    vector<Edge> edges;
    vector<int> execution_order;
    vector<double> graph_inputs;
    vector<double> graph_outputs;
    
    vector<pair<int, int>> input_mapping;
    vector<pair<int, int>> output_mapping;

    void build_execution_order() {

        vector<vector<int>> adj_list(vertices.size());
        
        for(const auto& edge : edges) {

            adj_list[edge.out_vertex_id].push_back(edge.inp_vertex_id);
        }
        
        Graph sorter(adj_list);
        execution_order = sorter.topological_sort();
        
    }
    
    void build_port() {
        input_mapping.clear();
        output_mapping.clear();
        

        for(int vertex_id = 0; vertex_id < vertices.size(); ++vertex_id) {
            for(int port_id = 0; port_id < vertices[vertex_id]->num_inputs(); ++port_id) {
                bool is_connected = false;
                for(const auto& edge : edges) {
                    if(edge.inp_vertex_id == vertex_id && edge.inp_port_id == port_id) {
                        is_connected = true;
                        break;
                    }
                }
                if(!is_connected) {
                    input_mapping.push_back({vertex_id, port_id});
                }
            }
        }
        
        for(int vertex_id = 0; vertex_id < vertices.size(); ++vertex_id) {
            for(int port_id = 0; port_id < vertices[vertex_id]->num_outputs(); ++port_id) {
                bool is_connected = false;
                for(const auto& edge : edges) {
                    if(edge.out_vertex_id == vertex_id && edge.out_port_id == port_id) {
                        is_connected = true;
                        break;
                    }
                }
                if(!is_connected) {
                    output_mapping.push_back({vertex_id, port_id});
                }
            }
        }
        
        graph_inputs.resize(input_mapping.size(), 0.0);
        graph_outputs.resize(output_mapping.size(), 0.0);
    }

public:

    void set_data(vector<Vertex*> vertex_ptrs, const vector<Edge>& new_edges) {
        vertices.clear();

        for(auto ptr : vertex_ptrs) {
            vertices.emplace_back(ptr);
        }

        edges = new_edges;
        
        build_execution_order();
        build_port();
        
    }
    
    int num_inputs() const override { 
        return input_mapping.size(); 
    }
    
    void set_input(int inp_idx, double inp_val) override {
        if(inp_idx < 0 || inp_idx >= input_mapping.size())
            throw out_of_range("Неверный индекс входа графа");
        graph_inputs[inp_idx] = inp_val;
    }
    
    int num_outputs() const override { 
        return output_mapping.size(); 
    }
    
    double get_output(int out_idx) override {
        if(out_idx < 0 || out_idx >= output_mapping.size())
            throw out_of_range("Неверный индекс выхода графа");
        return graph_outputs[out_idx];
    }
    
    void calc_value() override 
    {
        vector<vector<double>> vertex_inputs(vertices.size());
        for(int i = 0; i < vertices.size(); ++i) {
            vertex_inputs[i].resize(vertices[i]->num_inputs(), 0.0);
        }
        
        for(int i = 0; i < input_mapping.size(); ++i) {
            auto [vertex_id, port_id] = input_mapping[i];
            vertex_inputs[vertex_id][port_id] = graph_inputs[i];
        }
        

        for(int vertex_id : execution_order) {
            for(int port_id = 0; port_id < vertices[vertex_id]->num_inputs(); ++port_id) {
                vertices[vertex_id]->set_input(port_id, vertex_inputs[vertex_id][port_id]);
            }
            
    
            vertices[vertex_id]->calc_value();
            

            for(const auto& edge : edges) {
                if(edge.out_vertex_id == vertex_id) {
                    double output_value = vertices[vertex_id]->get_output(edge.out_port_id);
                    vertex_inputs[edge.inp_vertex_id][edge.inp_port_id] = output_value;
                }
            }
        }
        

        for(int i = 0; i < output_mapping.size(); ++i) {
            auto [vertex_id, port_id] = output_mapping[i];
            graph_outputs[i] = vertices[vertex_id]->get_output(port_id);
        }
    }
};

int main() {
    cout << "=== ТЕСТИРОВАНИЕ ===" << endl;
    
    cout << "1) Простой граф (два оператора сложения):" << endl;
    
    CalcGraph cg;
    vector<Vertex*> vertex;
    vector<Edge> edges;
    
    vertex.push_back(new PlusOperator);
    vertex.push_back(new PlusOperator);
    
    edges.push_back(Edge{0, 0, 1, 0});
    
    cg.set_data(vertex, edges);
    
    cg.set_input(0, 1.0);
    cg.set_input(1, 2.0);
    cg.set_input(2, 3.0); 
    
    cg.calc_value();
    
    cout << "Результат: " << cg.get_output(0) << endl;
    
    cout << "2) ИСПРАВЛЕННЫЙ сложный граф:" << endl;
    
    CalcGraph cg2;
    vector<Vertex*> vertex2;
    vector<Edge> edges2;
    
    vertex2.push_back(new PlusOperator);
    vertex2.push_back(new MultiplyOperator);
    vertex2.push_back(new MultiplyOperator);
    vertex2.push_back(new PlusOperator);
    
    edges2.push_back(Edge{0, 0, 1, 0});
    edges2.push_back(Edge{0, 0, 2, 0});
    edges2.push_back(Edge{1, 0, 3, 0});
    edges2.push_back(Edge{2, 0, 3, 1}); 
    
    cg2.set_data(vertex2, edges2);
    
    cg2.set_input(0, 1.0);
    cg2.set_input(1, 2.0);
    cg2.set_input(2, 3.0); 
    cg2.set_input(3, 4.0);
    
    cg2.calc_value();
    
    
    cout << "Результат: " << cg2.get_output(0) << endl;
    
    cout << "3) Простой граф умножения:" << endl;
    
    CalcGraph cg3;
    vector<Vertex*> vertex3;
    vector<Edge> edges3;
    
    vertex3.push_back(new MultiplyOperator); 
    
    cg3.set_data(vertex3, edges3);
    
    cg3.set_input(0, 5.0);
    cg3.set_input(1, 3.0); 
    
    cg3.calc_value();
    
    cout << "Результат: " << cg3.get_output(0) << endl;
    
    
    cout << "4) Тест на обнаружение циклов:" << endl;
    
    try {
        CalcGraph cg4;
        vector<Vertex*> vertex4;
        vector<Edge> edges4;
        
        vertex4.push_back(new PlusOperator); 
        vertex4.push_back(new PlusOperator); 
        

        edges4.push_back(Edge{0, 0, 1, 0});
        edges4.push_back(Edge{1, 0, 0, 0}); 
        
        cg4.set_data(vertex4, edges4);
        cout << "ОШИБКА: Цикл не обнаружен!" << endl;
    } 
    
    catch (const exception& e) {
        cout << "✓ Цикл обнаружен: " << e.what() << endl;
    }
    
    return 0;
}