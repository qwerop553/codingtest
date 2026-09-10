
main()
fun main(){
    val solution = Solution()
    val ss = solution.solution("CBD", listOf("BACDE", "CBADF", "AECB", "BDA"))
    println(ss)
}

class Solution {
    fun solution(skill: String, skill_trees: List<String>): Int{
        var ans = 0
        for (tree in skill_trees){
            var j = 0
            for ((i, element) in tree.withIndex()) {
                if (element in skill)
                    if (element == skill[j]) j++
                    else break

                if (i == tree.length - 1) {
                    ans += 1
                }
            }
        }
        return ans
    }
}

