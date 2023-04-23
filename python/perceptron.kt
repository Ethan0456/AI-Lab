class Perceptron(
    val num_input: Int,
    val x: List<Double>,
    val y: List<Double>,
    val w: List<Double>,
    val b: Double,
    val activation: (Double)->Double
) {
    fun fit(): List<Double> {
        var ls = mutableListOf<Double>()
        for (i in 0..num_input+1) {
            ls.add(x[i] * w[0] + y[i] * w[1] + b)
        }
        val out = ls.map{ x -> activation(x) }
        return out
    }
}

fun main() {
    val x = listOf(1.0,0.0,1.0,0.0)
    val y = listOf(0.0,0.0,1.0,1.0)
    val w = listOf(0.5,0.5)

    val or_per = Perceptron(
        num_input = 2,
        x = x,
        y = y,
        w = w,
        b = -0.25,
        activation = { a -> 
            if (a>0) 1.0 else 0.0
        } 
    )
    println("x = $x")
    println("y = $y")
    println("x or y = ${or_per.fit()}")

    println()

    val and_per = Perceptron(
        num_input = 2,
        x = x,
        y = y,
        w = w,
        b = -0.75,
        activation = { a -> 
            if (a>0) 1.0 else 0.0
        } 
    )
    println("x = $x")
    println("y = $y")
    println("x and y = ${and_per.fit()}")
}