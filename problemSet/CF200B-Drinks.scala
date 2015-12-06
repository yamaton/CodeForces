/**
  * 200 B. Drinks
  *
  * Created by yamaton on 11/19/15.
  */

object CF200B {

  def main(args: Array[String]) {
    val n = io.StdIn.readInt()
    val xs = io.StdIn.readLine.split(" ").map(_.toInt).toList
    assert(xs.length == n)
    val ans = solve(xs)
    println("%.12f".format(ans))
  }

  def solve(xs: List[Int]): Double = {
    xs.sum.toDouble / xs.length
  }

}