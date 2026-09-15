#include <string>
#include <vector>
#include <set>
using namespace std;

vector<string> U, B;
set<int> result;

bool match(const string& ban, const string& user){
    if (ban.size() != user.size()) return false;
    for (int i = 0; i < ban.size(); i++){
        if (ban[i] == '*') continue;
        if (ban[i] != user[i]) return false;
    }
    return true;
}

void dfs(int idx, int mask){
    if (idx == B.size()){
        result.insert(mask);
        return;
    }
    for (int i = 0; i < U.size(); i++){
        if ((mask & (1 << i)) != 0) continue;
        if (!match(B[idx], U[i])) continue;
        dfs(idx + 1, mask | (1 << i));
    }
}

int solution(vector<string> user_id, vector<string> banned_id){
    U = user_id;
    B = banned_id;
    dfs(0, 0);
    return result.size();
}