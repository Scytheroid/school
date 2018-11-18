public class Kvadraticka {
	public static void main(String[] args) {

		double a = Double.parseDouble(args[0]);
		double b = Double.parseDouble(args[1]);
		double c = Double.parseDouble(args[2]);
		
		//Overovani diskriminantu
		double d = b*b - 4*a*c;
		if (d > 0) {
			System.out.printf("Koreny rovnice jsou %f a %f",
			((b + Math.sqrt(d))/2*a),
			((b - Math.sqrt(d))/2*a));
		}
		else if ((d < 0.00001) || (d > -0.00001)) {
			System.out.printf("Koren rovnice je 0");
		}
		else {System.out.printf("Rovnice nema reseni");}
	}
}
