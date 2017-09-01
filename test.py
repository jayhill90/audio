import Nsound as ns

square = ns.Square(100, 3)
b = ns.Buffer()
b << square.generate(3.0, 1.0)
b.plot("Square wave") 


b.Plotter()
