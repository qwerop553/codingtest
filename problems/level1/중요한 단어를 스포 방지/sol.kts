#!/usr/bin/env kotlin
message = "here is muzi here is a secret message"
spoiler_range = [[0, 3], [23, 28]]

val m = message.length
val s = spoiler_range.size
val spoiled: HashMap<String, Integer>
val normal: HashMap<String, Int>

while (i< message.length){
    if (message[i] == ' ') { i++; continue }
    val s = i
    while (i < message.length && message[i] != ' ') i++
    val e = i - 1

    while (p < m && spoiler_range[p][1] < s) p++
    while (q < m && spoiler_range[q][0] <= e) q++

    val id = ids.getOrPut(message.substring(s, e + 1)){ ids.size }
    (if (p < q) spoiled or normal).add(id)
}
println(spoiled - normal)
