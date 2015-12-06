/**
  * Codeforces Round #332 (Div. 2)
  *
  * Problem 599 B. .
  *
  * author:  yamaton
  * date:    2015-11-20
  *
  */

object CF599B {
  def solve(fs: List[Int], bs: List[Int], n: Int, m: Int): (String, List[Int]) = {
    val setFs = fs.toSet
    val setBs = bs.toSet
    val ys = fs.filter(setBs.contains(_))
    val d = fs.zipWithIndex.filter({case (fst, snd) => bs.contains(fst)}).toMap

    if (setBs.exists(!setFs.contains(_))) {
      ("Impossible", List())
    } else if (ys.length != ys.toSet.size) {
      ("Ambiguity", List())
    } else {
      ("Possible", for (b <- bs) yield d(b) + 1)
    }
  }

  def main(args: Array[String]) {
    val Array(n, m) = io.StdIn.readLine().split(" ").map(_.toInt)
    val fs = io.StdIn.readLine().split(" ").map(_.toInt).toList
    val bs = io.StdIn.readLine().split(" ").map(_.toInt).toList
    assert(fs.length == n)
    assert(bs.length == m)

    val (msg, lst) = solve(fs, bs, n, m)
    println(msg)
    if (!lst.isEmpty) 
        println(lst.mkString(" "))
  }
}
