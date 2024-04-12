package lectures.part1basics

object Expressions extends App {//extends App codun runable olmasini sagliyor.
  val x = 1+2//EXPRESSION
  println(x)
  println(2+4*9)
//instruction (do) vs expression (value)
  val aCondition =true
  val aConditionedValue = if(aCondition) 5 else 3//if is an expression
  println(aConditionedValue)
  println(1+3)
  //there are loops in scala but they are discouraged to be used.
  var i =0
  while (i< 10){
    println(i)
    i +=1
  }
//never write a while loop again
//everythinh in scala is an expression!!

  //val aWeirdValue = (aVariable = 3)//Unit ===void
  //println(aWeirdValue)
  //side effects: println() whiles reassigning
  //code blocks
  //code block is an expression
  val aCodeBlock = {
    val y = 2
    val z = y + 1
    if(z>2) "hello" else "goodbye"

  }
  //val anotherValue = z+1 //bu gorunmeyecek cunku Z yi daha once codeblock da tanimladik.
//1. difference betwwen "hello world" and "println("hello world")
//2.
  val someValue= {
    2 < 3
  }
  val someOtherValue = {
    if(someValue) 239 else 986
    42
  }
  println(someValue)
  println(someOtherValue)
}
//1. "hello world" is value println side effect that writes things to console 