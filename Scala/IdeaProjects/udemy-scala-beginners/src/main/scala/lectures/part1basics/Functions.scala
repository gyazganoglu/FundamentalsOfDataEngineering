package lectures.part1basics

object Functions extends App {
  def aFunction(a:String, b:Int):String = {
    a + " " + b
  }
//kume parantezi sart degil ama neden olmasin
  println(aFunction("hello", 3))
  //calling a function is also an expression
  //a function can be parameterless
  def aParameterlessFunction():Int = 42
  println(aParameterlessFunction())

  def aRepeatedFunction(aString:String, n:Int) : String ={
    if(n==1) aString
    else aString + aRepeatedFunction(aString, n-1)
  }
  println(aRepeatedFunction("hello",3))
  //scala'da loop yerine recursive function kullanmaliyiz.
  //eger return type anlasiliyorsa mesela aFunction hep String getirir.
  // ama recursive function icin belirtmemiz gerekiyor
  //Unit bir return type boyle olunca sadece side effect uretir.

  def aFunctionWithSideEffects(aString: String):Unit = println(aString)

  def aBigFunction(n: Int): Int = {
    def aSmallerFunction(a: Int, b: Int): Int = a + b

    aSmallerFunction(n, n - 1)

  }
  println(aBigFunction(9))

  def aGreatingFunction(name:String, age: Int)= {
    println("Hi, My name is " + name + " and I am " + age +" years old.")
  }
  aGreatingFunction("Kaan", 4)
  def aFactorialFunction (n:Int): Int ={
    if ((n==1)|(n==0)) 1
    else n * aFactorialFunction(n-1)

  }
  println(aFactorialFunction(0))

  def aFibonacciFunction(n:Int): Int={
    if (n<=2) 1
    else (aFibonacciFunction(n-1) + aFibonacciFunction(n-2))
  }
  println(aFibonacciFunction(8))

  def isPrime(n:Int): Boolean = {
    def primeUntil(t:Int): Boolean = {
      if (t <= 1) true
      else n % t != 0 && primeUntil(t - 1)
    }
    primeUntil(n/2)
    

  }
  println(isPrime(2003))


}

