import AnimalsPackage.*;

class TestAnimals {
	public static void main(String[] args) {
		Cat c = new Cat(3.5, "chicken");
		System.out.println("The cat eats: ");
		c.printFoods();
		System.out.println("The cat weighs " + c.weight + "kg");
		System.out.println("The cat says: ");
		c.makeSound();
		
		System.out.println("====================");
		
		Dog d = new Dog(7, "kibble");
		System.out.println("The dog eats: ");
		d.printFoods();
		System.out.println("The dog weighs " + d.weight + "kg");
		System.out.println("The dog says: ");
		d.makeSound();

		System.out.println("====================");
		
		Lion l = new Lion(190, "zebra");
		System.out.println("The lion eats: ");
		l.printFoods();
		System.out.println("The lion weighs " + l.weight + "kg");
		System.out.println("The lion says: ");
		l.makeSound();
		
		System.out.println("====================");
		
		Wolf f = new Wolf(50, "deer");
		System.out.println("The wolf eats: ");
		f.printFoods();
		System.out.println("The wolf weighs " + f.weight + "kg");
		System.out.println("The wolf says: ");
		f.makeSound();
		
	}
}