main()
fun main(){

}

class Solution {
    fun solution(grid: Array<IntArray>){

    }

    // 연결하고, 해당 블록이 잘 되는지 확인하고, 다음 함수를 호출한다
    // dfs(grid, 0, 0)
    fun dfs(grid: Array<IntArray>, from: Pair<Int, Int>, to: Pair<Int, Int>){
        // 이미 물건이 있는 경우
        val y = from.first; val x = from.second
        val a = to.first; val b = to.second
        if (grid[a][b] != 0) {
            if (a==b && y!=x && grid[a][b]==1){
                dfs(grid, Pair(a, b), Pair())
            }
        }
    }

        // 상관이 없는 경우

}