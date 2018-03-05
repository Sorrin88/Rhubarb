package AnimalsPackage;
public class Dog extends Canine {
	public Dog() {
		super(5.6);
		this.addFood("Bones");
		this.addFood("Treats");
		packSize = 2;
	}

	public Dog(double weight) {
		super(weight);
		packSize = 2;
	}

	public Dog(double weight, String food) {
		super(weight);
		this.addFood(food);
		packSize = 2;
	}

	@Override
	public void makeSound() {
		System.out.println("woof");
	}
}