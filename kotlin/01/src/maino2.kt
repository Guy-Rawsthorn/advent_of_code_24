import java.io.File
import kotlin.math.absoluteValue

fun main() {
    var input: List<String> = File("input/test-day02.txt").readLines()
    part1(input)
}

fun part1(input: List<String>) {
    for (line: String in input) {
        val numbers: List<Int> = line.split(" ").map { it.toInt() }
        println(numbers)
        val safe: Boolean = isLineSafe(numbers)
    }
}

fun isLineSafe(numbers: List<Int>): Boolean {
    var safe = true
    var isAscending = true
    var isDescending = true

    for (i: Int in 0..<numbers.lastIndex) {
        val a = numbers[i]
        val b = numbers[i + 1]
        safe = safe && ((a - b).absoluteValue <= 3)
        when {
            a < b -> isDescending = false
            a > b -> isAscending = false
            else -> {
                isAscending = false
                isDescending = false
            }
        }
    }
    return safe && (isAscending || isDescending)
}