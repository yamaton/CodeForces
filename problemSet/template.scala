/**
  * Codeforces Round #332 (Div. 2)
  *
  * Problem 599 A.
  *
  * author:  yamaton
  * date:    2015-11-20
  *
  */

object CF599A {
  def solve(xs: List[Int], n: Int): Int = {
    
  }


  def main(args: Array[String]) {
    val n = io.StdIn.readInt()
    val Array(a, b) = io.StdIn.readLine.split(" ").map(_.toInt)
    val xs = io.StdIn.readLine.split(" ").map(_.toInt).toList
    assert(xs.length == n)
    val ans = solve(xs, n, a, b)
    println(ans)
  }
}
