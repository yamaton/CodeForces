/**
  * Codeforces Round #332 (Div. 2)
  *
  * Problem 599 A. Patrick and Shopping
  *
  * author:  yamaton
  * date:    2015-11-20
  *
  */

object CF599A {
  def solve(d1: Int, d2: Int, d3: Int): Int = {
    List(d1 + d2 + d3,
         2 * (d1 + d2),
         2 * (d2 + d3),
         2 * (d3 + d1)).min
  }

  def main(args: Array[String]) {
    val List(d1, d2, d3) = io.StdIn.readLine().split(" ").map(_.toInt).toList
    val ans = solve(d1, d2, d3)
    println(ans)
  }
}
