package AnimalsPackage;
import java.util.ArrayList;

public class Cat extends Feline {
	public Cat() {
		super();
		this.addFood("Mice");
		this.addFood("Birds");
		lives = 7;

		// this.foods.add("Mice");
		// this.foods.add("Birds");
	}

	public Cat(double weight) {
		super(weight);
		lives = 7;
	}

	public Cat(double weight, String food) {
		super(weight);
		this.addFood(food);
		lives = 7;
	}

	@Override
	public void makeSound() {
		System.out.println("meow");
	}
	
}