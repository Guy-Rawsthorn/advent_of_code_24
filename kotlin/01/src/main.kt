import kotlin.io.path.Path
import kotlin.io.path.readLines
import kotlin.math.abs

fun readInput(): List<String> = Path("./test-input.txt").readLines()

fun main() {
    val lines = readInput()

    val (left, right) = lines.map { line ->
        val first = line.substringBefore(" ").toInt()
        val second = line.substringAfterLast(" ").toInt()
        first to second
    }.unzip()

    val sumResult = left.sorted().zip(right.sorted()).map{ (first, second) ->
        abs(first - second)
    }.sum()

//    val (longLeft, longRight) = left.zip(right).map {(first, second) ->
//        first.toLong() to second.toLong()
//    }.unzip()
//
//    val frequencies: Map<Long, Int> = longRight.groupingBy { it }.eachCount()
//
//    left.fold(0L) { acc: Long, num: Long ->
//        acc + num * frequencies.getOrDefault(num, 0)
//    }.also(block:::println)





    println(sumResult)
}
