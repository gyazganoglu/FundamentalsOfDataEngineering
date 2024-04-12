package lectures.part1basics

object ValusesVariableTypes extends App{

  val x: Int= 42
  println(x)

  //Vals are inmutable
  //Types are not mandatory if we don't put compiler will assign sth that would work.
  val aString: String = "Hello";
  // semi columns are not mandatory if we put we can go on with sth else. But not recomended.
  val aBoolean: Boolean =false
  val aChar: Char = 'a'
  val aShort: Short = 49 //Short number
  val aLong: Long = 5678765544433
  val aFloat: Float = 2.0f
  val aDouble: Double = 3.14

  var aVariable:Int = 4
  aVariable = 5 //side effects
}
